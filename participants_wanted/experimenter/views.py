from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExprProfile, Experiment
from student.models import StudentInfo, Demsurv

from .forms import ExprForm, ExprProfileForm, CreateExpr


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('experimenter:home'))

def getall(request):
    expr = Experiment.objects.all()
    json = serializers.serialize('json', expr)
    return HttpResponse(json, content_type='application/json')


def index(request):
    return render(request, 'expr/index.html')

@login_required()
def home(request):
    try:
        i = Demsurv.objects.get(user=request.user)
        return render(request, 'student/home.html')
    except ObjectDoesNotExist:
        print()
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
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user = authenticate(username=expr_form.cleaned_data['username'],
                                password=expr_form.cleaned_data['password'],
                                )
            login(request, user)
            response = redirect(reverse('experimenter:home'))
            return response
        else:
            print(expr_form.errors, exprp_form.errors)
    else:
        expr_form = ExprForm()
        exprp_form = ExprProfileForm
    return render(request, 'expr/register.html', context={'expr_form': expr_form, 'exprp_form':exprp_form, 'registered': registered})


def expr_lgoin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                try:
                    i = ExprProfile.objects.get(user=user)
                except ObjectDoesNotExist:
                    error = "Experimenter Login Only, Student account used"
                    return render(request, 'expr/login.html', context={'error':error})
                login(request, user)
                return redirect(reverse('experimenter:home'))
            else:
                return HttpResponse('account disabled')
        else:
            error = "Invalid Login Details"
            return render(request, 'expr/login.html', context={'error': error})
    else:
        return render(request, 'expr/login.html')


@login_required
def createExperemnt(request):
    created = False
    if request.method == 'POST':
        cexpr_form = CreateExpr(request.POST)
        user = request.user
        if cexpr_form.is_valid():
            expr = cexpr_form.save(commit=False)
            expr.user = user
            expr.save()
            created = True
            response = redirect(reverse('experimenter:home'))
            return response
        else:
            print(CreateExpr.errors)
    else:
        cexpr_form = CreateExpr
    return render(request, 'expr/createexpr.html',
                  context={'cexpr_form': cexpr_form, 'created': created})


@login_required
def accept(request):
    try:
        request.GET['expr']
    except Exception as e:
        return render(request, 'home/index.html')
    expr_name = request.GET['expr']
    student = request.GET['student']
    try:
        expr = Experiment.objects.get(name=expr_name)
        user = User.objects.get(username=student)
        expr.students.remove(user)
        expr.accepted.add(user)
        expr.num_current = expr.num_current + 1
        if expr.num_req == expr.num_current:
            expr.expr_full = True
        s_i = StudentInfo.objects.get(user__username=student)
        s_i.notifications = s_i.notifications + 1
        s_i.currentexpr.add(expr)
        s_i.bidexpr.remove(expr)
        s_i.save()
        expr.save()

    except ObjectDoesNotExist:
        return HttpResponse(-1)
    return HttpResponse()


@login_required
def decline(request):
    try:
        request.GET['expr']
    except Exception as e:
        return render(request, 'home/index.html')
    expr_name = request.GET['expr']
    student = request.GET['student']
    try:
        expr = Experiment.objects.get(name=expr_name)
        user = User.objects.get(username=student)
        expr.students.remove(user)
        s_i = StudentInfo.objects.get(user__username=student)
        s_i.bidexpr.remove(expr)
        s_i.decexpr.add(expr)
        s_i.decline = s_i.decline + 1
        s_i.save()
        expr.save()
    except ObjectDoesNotExist:
        return HttpResponse(-1)
    return HttpResponse()

@login_required
def close(request):
    try:
        request.GET['expr']
    except Exception as e:
        return render(request, 'home/index.html')
    name = request.GET['expr']
    li = []
    expr = Experiment.objects.get(name=name)
    expr.expr_done = True
    expr.save()
    for s in expr.accepted.all():
        s_i = StudentInfo.objects.get(user=s)
        s_i.currentexpr.remove(expr)
        s_i.pastexpr.add(expr)
        s_i.save()
    return HttpResponse()


