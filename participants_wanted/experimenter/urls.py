from django.contrib import admin
from django.urls import path
from . import views


app_name = 'experimenter'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]
