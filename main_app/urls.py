from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trash/', views.trash_index, name='trash_index'),
    path('trash/<int:trash_id>/', views.trash_detail, name='trash_detail'),
    path('trash/create/', views.trash_create.as_view(), name='trash_create'),
    path('trash/<int:pk>/update/', views.trash_update.as_view(), name='trash_update'),
    path('trash/<int:pk>/delete/', views.trash_delete.as_view(), name='trash_delete'),
    path('trash/<int:trash_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('trash/<int:trash_id>/assoc_flair/<int:flair_id>', views.assoc_flair, name='assoc_flair'),
    path('trash/<int:trash_id>/unassoc_flair/<int:flair_id>', views.unassoc_flair, name='unassoc_flair'),
    path('trash/<int:trash_id>/add_photo/', views.add_photo, name='add_photo'),
    path('flair/', views.flair_list.as_view(), name='flair_list'),
    path('flair/<int:pk>/', views.flair_detail.as_view(), name='flair_detail'),
    path('flair/create/', views.flair_create.as_view(), name='flair_create'),
    path('flair/<int:pk>/update/', views.flair_update.as_view(), name='flair_update'),
    path('flair/<int:pk>/delete/', views.flair_delete.as_view(), name='flair_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
