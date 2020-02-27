
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'student'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('demsurv/', views.demsurv, name='demsurv'),
    path('profile/', views.profile, name='profile'),
    path('makebid/', views.makebid, name='makebid'),
    path('displaydetails/', views.displaydetails, name='displaydetails')
]
