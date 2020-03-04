from django import forms
from django.contrib.auth.models import User
from .models import ExprProfile, Experiment

class DateInput(forms.DateInput):
    input_type = 'date'


class ExprForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        help_texts = {
            'username': None,
        }

class ExprProfileForm(forms.ModelForm):
    class Meta:
        model = ExprProfile
        fields = ('title', 'school', 'webpage', 'schoolemail', 'publicnumber')


class CreateExpr(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ('name', 'details', 'price', 'start_date', 'end_date', 'num_req', 'age_req', 'lang_req', 'ed_req')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }