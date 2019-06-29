from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields
from datetime import date
# Create your models here.

class Flair(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('flair_detail',
            kwargs={'pk': self.id}
            )

class Trash(models.Model):
    name = models.CharField(max_length=100)
    location = map_fields.AddressField(max_length= 200)
    description = models.TextField(max_length=250)
    time = models.DateTimeField(auto_now=True)
    flair = models.ManyToManyField(Flair)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',
            kwargs={'trash_id': self.id}
            )

class Seen(models.Model):
    time_seen = models.DateTimeField('Last Seen')
    was_there = models.BooleanField(default=False)
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trash.name} was still there on {self.time_seen}"

    class Meta:
        ordering = ['-time_seen']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    trash = models.ForeignKey(Trash, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for trash_id: {self.trash_id} @ {self.url}'
