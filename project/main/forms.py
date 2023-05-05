from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import MyRegisteredUser
from django.forms.widgets import EmailInput, PasswordInput, TextInput, CheckboxInput, Select, RadioSelect
from django.core.validators import RegexValidator, EmailValidator

# This is my user registration form:


class MyUserRegistrationForm(forms.ModelForm):
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
        model = MyRegisteredUser
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

# This is a class for default user registration form:


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label="username", widget=TextInput(attrs={"class": "form-control", "placeholder": "Username"}))
    password1 = forms.CharField(label="password", widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Password"}))
    
    password2 = forms.CharField(label="password confirm", widget=PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}))
 
    class Meta:
        # Specify the default model - User:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

        widgets = {
            'first_name': TextInput(attrs={
                "class": "form-control",
                "placeholder": "First name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "placeholder": "email@gmail.com"
            }),
            'last_name': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Middle name"
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']