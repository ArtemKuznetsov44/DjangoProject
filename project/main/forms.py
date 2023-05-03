from django import forms
from .models import User
from django.forms.widgets import EmailInput, PasswordInput, TextInput, CheckboxInput, Select, RadioSelect
from django.core.validators import RegexValidator, EmailValidator


class UserRegistrationForm(forms.ModelForm):
    # Our widgets dictionary works only with fields from model 
    # and only for fields which your not specified in forms again before Meta class:
    
    first_name = forms.CharField(
        validators=[RegexValidator(
            regex='^[A-Z][a-zA-Z]{1,15}$', message="Your first name is in incorrect format!")],
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your first name"
        }))

    middle_name = forms.CharField(
        validators=[RegexValidator(
            regex='^[A-Z][a-zA-Z]{1,15}$', message="Your middle name is in incorrect fromat!")],
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your middle name"
        }))

    password = forms.CharField(
        validators=[RegexValidator(
            regex='^(?=.*\d)(?=.*[A-Z])(?=.*\W).{1,16}$', message="Your password is in incorrect format!")],
        widget=PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Your password"
        }))

    login = forms.CharField(
        validators=[RegexValidator(
            regex='^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', message="Your login is in incorrect format!")],
        widget=TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your login"
        }))

    email = forms.CharField(
        validators=[EmailValidator(
            message="Your emain is in incorrect format!")],
        widget=EmailInput(attrs={
            "class": "form-control",
            "placeholder": "email@gmail.com"
        }))

    accept_rules = forms.BooleanField(
        required=True, widget=CheckboxInput(attrs={"class": "form-check-input"}))

    gender = forms.ChoiceField(
        choices=(('man', 'Man'), ('woman', 'Woman')), widget=RadioSelect)

    age = forms.ChoiceField(choices=(('under_18', 'Under 18 years old'), ('over_18',
                            'Over 18 years old')), widget=Select(attrs={"class": "form-select form-select-sm"}))

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
                  # The next field is not from model it is only in currect form, but we need to specify it in current list to show it:
                  'accept_rules']

        widgets = {
            "to_be_informed": CheckboxInput(attrs={
                "class": "form-check-input"
            }),
        }
