from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExprProfile, Experiment
from student.models import StudentInfo

from .forms import ExprForm, ExprProfileForm


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('experimenter:index'))



def index(request):
    return render(request, 'expr/index.html')


def home(request):
    expr = Experiment.objects.filter(user=request.user)
    dict = {}
    for e in expr:
        dynamicname = []
        students = e.students.all()
        for s in students:
            dynamicname.append(s.username)
        dict[e.name] = dynamicname
    return render(request, 'expr/home.html', context={'expr':expr, 'dict': dict})


def register(request):
    registered = False
    if request.method == 'POST':
        expr_form = ExprForm(request.POST)
        exprp_form = ExprProfileForm(request.POST)

        if expr_form.is_valid() and exprp_form.is_valid():
            user = expr_form.save()
            user.set_password(user.password)
            user.save()
            profile = exprp_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(expr_form.errors, exprp_form.errors)
    else:
        expr_form = ExprForm()
        exprp_form = ExprProfileForm
    return render(request, 'expr/register.html', context={'expr_form': expr_form, 'exprp_form':exprp_form, 'registered':registered})


def expr_lgoin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        try:
            i = ExprProfile.objects.get(user=user)
        except ObjectDoesNotExist:
            return HttpResponse('This is the expr login, you have a student account')
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('experimenter:index'))
            else:
                return HttpResponse('account disabled')
        else:
            print(f'Invalid login detials')
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'expr/login.html')



# Notify (a user has applied for study)

# See bids:
# see list of all applicants & applicants' info
# accept or decline an applicant (y/n accept bid)

@login_required
def accept(request):
    expr_name = request.GET['expr']
    student = request.GET['student']
    try:
        expr = Experiment.objects.get(name=expr_name)
        user = User.objects.get(username=student)
        expr.students.remove(user)
        s_i = StudentInfo.objects.get(user__username=student)
        s_i.currentexpr.add(expr)
        s_i.bidexpr.remove(expr)
        s_i.save()
        expr.save()

    except ObjectDoesNotExist:
        return HttpResponse(-1)
    return HttpResponse()

@login_required
def decline(request):
    expr_name = request.GET['expr']
    student = request.GET['student']
    try:
        expr = Experiment.objects.get(name=expr_name)
        user = User.objects.get(username=student)
        expr.students.remove(user)
        s_i = StudentInfo.objects.get(user__username=student)
        s_i.bidexpr.remove(expr)
        s_i.save()
        expr.save()
    except ObjectDoesNotExist:
        return HttpResponse(-1)
    return HttpResponse()