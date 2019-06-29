from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trash, Seen, Flair
from .forms import SeenForm
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'ccatcollector'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def trash_index(request):
    trash = Trash.objects.all()
    return render(request, 'trash/index.html', { 'trash': trash })

def trash_detail(request, trash_id):
    trash = Trash.objects.get(id=trash_id)
    flair_not_on_trash = Flair.objects.exclude(id__in = trash.flair.all().values_list('id'))
    seen_form = SeenForm
    return render(request, 'trash/trash_detail.html', {
        'trash': trash,
        'seen_form': seen_form,
        'flair': flair_not_on_trash
        })

class trash_create(CreateView):
    model = Trash
    fields = ['name', 'description', 'location']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class trash_update(UpdateView):
    model = Trash
    fields = ['name', 'description', 'location']

class trash_delete(DeleteView):
    model = Trash
    success_url = '/trash/'

def add_sighting(request, trash_id):
    form = SeenForm(request.POST)
    if form.is_valid():
        new_sighting = form.save(commit=False)
        new_sighting.trash_id = trash_id
        new_sighting.save()
    return redirect('trash_detail', trash_id=trash_id)

def assoc_flair(request, trash_id, flair_id):
    Trash.objects.get(id=trash_id).flair.add(flair_id)
    return redirect('trash_detail', trash_id=trash_id)

def unassoc_flair(request, trash_id, flair_id):
    Trash.objects.get(id=trash_id).flair.remove(flair_id)
    return redirect('trash_detail', trash_id=trash_id)

class flair_list(LoginRequiredMixin, ListView):
    model = Flair

class flair_detail(DetailView):
    model = Flair

class flair_create(LoginRequiredMixin, CreateView):
    model = Flair
    fields = '__all__'

class flair_update(LoginRequiredMixin, UpdateView):
    model = Flair
    fields = ['name', 'color']

class flair_delete(LoginRequiredMixin, DeleteView):
    model = Flair
    success_url = '/trash/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trash_index')
        else:
            error_message = 'Invalid credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_photo(request, trash_id):
    photo_file = request.FILES.get('photo_file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, trash_id=trash_id)
            photo.save()
        except:
            print('An error occured uploading file to S3')
        return redirect('trash_detail', trash_id=trash_id)
