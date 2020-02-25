from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import ExprProfile

from .forms import ExprForm, ExprProfileForm

def index(request):
    return render(request, 'expr/index.html')

# copied from Student
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
