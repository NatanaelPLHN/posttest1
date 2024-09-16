from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('katalog', views.katalog),
    path('about', views.about),

]
