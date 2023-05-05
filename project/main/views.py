from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MyRegisteredUser
from .forms import MyUserRegistrationForm, RegisterUserForm
from django.contrib.auth.hashers import make_password
# from django.http import HttpResponse # This class is used for generate HTTP-format responses (answers)

# Create your views here.

# To my mind it is like an action in Yii (maybe it is a worse statement)
# The request param is required (обязетельный):
def home(request): 
    # return HttpResponse("<h1>Main page</h1>")
    return render(request, template_name='main/home.html')
    # Do nothing:
    # pass
    
def my_registration(request): 
    if request.method == 'POST': 
        # Create the same form object but with a data from POST array:
        form = MyUserRegistrationForm(request.POST)
        if form.is_valid(): 
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            email = form.cleaned_data.get('email')
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            gender = form.cleaned_data.get('gender')
            age = form.cleaned_data.get('age')
            to_be_informed = form.cleaned_data.get('to_be_informed')
            
            hash_password = make_password(password)
            
            new_user = User()
            new_user.first_name = first_name
            new_user.middle_name = middle_name
            new_user.email = email
            new_user.password = hash_password
            new_user.gender = gender
            new_user.age = age
            if to_be_informed == True:
                new_user.to_be_informed = True
            
            new_user.save()
    else:
        form = MyUserRegistrationForm()
    
    data = {
        'form': form,
    }
    
    return render(request, template_name='main/my_registration.html', context=data) 

def my_authorization(request): 
    return render(request, template_name='main/my_authorization.html')

def default_registration(request): 
    # Checks that method is POST:
    if request.method == 'POST':
        # Get data from form:
        form = RegisterUserForm(request.POST)
        # If data is valid:
        if form.is_valid(): 
            # Create new uers with the data in form:
            new_user = form.save(commit=False)
            # Set the chosen password
            new_user.set_password(form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            form = RegisterUserForm()
            return render(request, template_name = 'main/default_registration.html', context={'form': form})
    else:
        form = RegisterUserForm()
        
    return render(request, template_name = 'main/default_registration.html', context={'form': form})

def default_authorization(request): 
    return render(request, template_name='main/default_authorization.html')