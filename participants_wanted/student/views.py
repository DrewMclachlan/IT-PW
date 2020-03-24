from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .forms import UserForm, DemsurvForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Demsurv, StudentInfo
from experimenter.models import Experiment
from django.core.exceptions import ObjectDoesNotExist
import json
from django.core import serializers

def mainhome(request):
    return render(request, 'home/index.html')

def viewall(request):
    acceptedexpr = []
    waitingexpr = []
    declined = []

    try:
        student = request.COOKIES.get('student')
        context = {'student':student}
        if student == None:
            raise Experiment
        ds = Demsurv.objects.get(user=request.user)
        s_i = StudentInfo.objects.get(user=request.user)
        for i in s_i.bidexpr.all():
            waitingexpr.append(i.id)

        for i in s_i.currentexpr.all():
            acceptedexpr.append(i.id)

        for i in s_i.decexpr.all():
            declined.append(i.id)

        context['declined'] = declined
        context['accepted'] = acceptedexpr
        context['waiting'] = waitingexpr
        context['demsurv'] = ds

        return render(request, 'home/viewall.html', context=context)
    except Exception as e:
        if type(e).__name__ == 'DoesNotExist':
            return HttpResponse('you must do the dem surv before bidding')
        else:
            return render(request, 'home/viewall.html')




@login_required
def home(request):
    expr = Experiment.objects.all()
    expr = expr.exclude(students__username=request.user)
    s_i = StudentInfo.objects.get(user=request.user)
    notif = s_i.notifications
    dec = s_i.decline
    acceptedexpr = []
    waitingexpr = []
    pastexpr = []
    s_i.notifications = 0
    s_i.decline = 0
    s_i.save()
    for i in s_i.bidexpr.all():
        waitingexpr.append(i)

    for i in s_i.currentexpr.all():
        acceptedexpr.append(i)

    for i in s_i.pastexpr.all():
        pastexpr.append(i)


    return render(request, 'student/home.html', context={'expr': expr, 'acceptedexpr':acceptedexpr, 'waitingexpr': waitingexpr, 'pastexpr':pastexpr, 'notif':notif, 'dec':dec})

@login_required
def user_logout(request):
    logout(request)
    response = redirect(reverse('student:home'))
    response.delete_cookie('student')
    return response


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            student_info = StudentInfo(user=user)
            student_info.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user = authenticate(username=user_form.cleaned_data['username'],
                                    password=user_form.cleaned_data['password'],
                                  )
            login(request, user)
            response = redirect(reverse('student:home'))
            response.set_cookie('student', 'true')
            return response
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'student/register.html', context={'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        try:
            i = StudentInfo.objects.get(user=user)
        except ObjectDoesNotExist:
            return HttpResponse('This is the student login, you have a expr account')
        if user:
            if user.is_active:
                login(request, user)
                response = redirect(reverse('student:home'))
                response.set_cookie('student', 'true')
                return response
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



# update to class views
@login_required
def makebid(request):
    expr_name = request.GET['expr_name']
    username = request.GET['username']
    u_id = request.GET['u_id']
    try:
        expr = Experiment.objects.get(name=expr_name)
        s_i = StudentInfo.objects.get(user_id=u_id)
    except ObjectDoesNotExist:
        return HttpResponse(-1)
    expr.students.add(User.objects.get(username=username))
    s_i.bidexpr.add(expr)
    expr.save()
    s_i.save()
    return HttpResponse(expr)


@login_required
def displaydetails(request):
    name = request.GET['name']
    try:
        demsurv = Demsurv.objects.get(user__username=name)
    except ObjectDoesNotExist:
        return HttpResponse(-1)
    ser_obj = serializers.serialize('json', [demsurv])
    return HttpResponse(ser_obj)



