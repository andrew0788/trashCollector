from django.forms import ModelForm
from .models import Seen

class SeenForm(ModelForm):
    class Meta:
        model = Seen
        fields = ['was_there', 'time_seen']
