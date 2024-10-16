from django.urls import path
from . import views 
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('katalog/', views.laptop_list, name='katalog'),
    path('create/', views.laptop_create, name='laptop_create'),
    path('update/<int:id_laptop>/', views.laptop_update, name='laptop_update'),
     path('laptop/delete/<int:id_laptop>/', laptop_delete, name='laptop_delete'),
     
]