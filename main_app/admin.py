from django.contrib import admin
from .models import Trash, Seen, Flair, Photo
# Register your models here.

admin.site.register(Trash)
admin.site.register(Seen)
admin.site.register(Flair)
admin.site.register(Photo)
