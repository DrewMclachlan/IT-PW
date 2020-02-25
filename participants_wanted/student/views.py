from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .forms import UserForm, DemsurvForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Demsurv, Experiment
from django.core.exceptions import ObjectDoesNotExist

def mainhome(request):
    return render(request, 'home/index.html')


@login_required
def home(request):
    expr = Experiment.objects.all()
    expr = expr.exclude(students__username=request.user)
    waitingexpr = Experiment.objects.filter(students__username=request.user)
    return render(request, 'student/home.html', context={'expr': expr, 'waitingexpr': waitingexpr})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('student:home'))


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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        ##need to add an aspect of checking for student satus
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('student:home'))
            else:
                return HttpResponse('student account disabled')
        else:
            print(f'Invalid login detials')
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'student/login.html')

@login_required
def demsurv(request):
    if request.user:
        user = request.user
        if request.method == 'POST':
            dem_form = DemsurvForm(request.POST)
            if dem_form.is_valid():
                surv = dem_form.save(commit=False)
                surv.user = user
                print(request.FILES)
                if 'picture' in request.FILES:
                    surv.picture = request.FILES['picture']
                surv.save()
                return redirect(reverse('student:home'))
            else:
                print(dem_form.errors)
        else:
            dem_form = DemsurvForm()
        return render(request, 'student/demsurvey.html', context={'dem_form': dem_form})
    else:
        print('not working')

@login_required
def profile(request):
    try:
        i = Demsurv.objects.get(user=request.user)
        context_dict = {}
        context_dict['info'] = i
        return render(request, 'student/profile.html', context=context_dict)
    except ObjectDoesNotExist:
        return HttpResponse("you must do the dem survey first!")



##update to class views
@login_required
def makebid(request):
    expr_name = request.GET['expr_name']
    username = request.GET['username']
    print(expr_name, username)
    try:
        expr = Experiment.objects.get(name=expr_name)
        print(expr._meta.fields)
    except ObjectDoesNotExist:
        return HttpResponse(-1)
    expr.save()
    expr.students.add(User.objects.get(username=username))

    return HttpResponse(expr)


