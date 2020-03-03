from django.contrib import admin
from django.urls import path
from . import views

app_name = 'experimenter'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.expr_lgoin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('accept/', views.accept, name='accept'),
    path('decline/', views.decline, name='decline'),
    path('getall/', views.getall, name='getall')

]
