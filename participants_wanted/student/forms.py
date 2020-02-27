from django import forms
from django.contrib.auth.models import User
from .models import Demsurv

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)



class DemsurvForm(forms.ModelForm):
    class Meta:
        model = Demsurv
        fields = ('sex', 'age', 'language', 'country', 'education', 'picture')

