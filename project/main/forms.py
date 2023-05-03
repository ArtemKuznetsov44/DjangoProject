from django import forms
from .models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput, CheckboxInput, Select, RadioSelect
from django.core.validators import RegexValidator, EmailValidator


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(validators=[RegexValidator()])
    accept_rules = forms.BooleanField(required=True ,widget=CheckboxInput(attrs={"class": "form-check-input"}))
    gender = forms.ChoiceField(choices=(('man', 'Man'), ('woman', 'Woman')), widget=RadioSelect)
    age = forms.ChoiceField(choices=(('under_18', 'Under 18 years old'), ('over_18', 'Over 18 years old')), widget=Select(attrs={"class": "form-select form-select-sm"}))

    class Meta:
        model = User
        fields = ['first_name',
                  'middle_name',
                  'email',
                  'login',
                  'password',
                  'age',
                  'gender',
                  'to_be_informed',
                  'accept_rules']


        widgets = {
            "first_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your first name"
            }),
            "middle_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your middle name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "email@gmail.com"
            }),
            "login": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your login"
            }),
            "password": PasswordInput(attrs={
                "class": "form-control",
                "placeholder": "Your password"
            }),
            "to_be_informed": CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }
