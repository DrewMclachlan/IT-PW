from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def home(request):
    return render(request, 'home/index.html')


def index(request):
    return render(request, 'student/index.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    print(user_form)
    return render(request, 'student/register.html', context={'user_form': user_form, 'registered': registered})
