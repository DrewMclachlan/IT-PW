from django import forms
from django.contrib.auth.models import User
from .models import ExprProfile

class ExprForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class ExprProfileForm(forms.ModelForm):
    class Meta:
        model = ExprProfile
        fields = ('title', 'school', 'webpage', 'schoolemail', 'publicnumber')