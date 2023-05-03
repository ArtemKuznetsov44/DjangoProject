from django.shortcuts import render
from .forms import UserRegistrationForm
# from django.http import HttpResponse # This class is used for generate HTTP-format responses (answers)

# Create your views here.

# To my mind it is like an action in Yii (maybe it is a worse statement)
# The request param is required (обязетельный):
def home(request): 
    # return HttpResponse("<h1>Main page</h1>")
    return render(request, template_name='main/home.html')
    # Do nothing:
    # pass
    
def registration(request): 
    form = UserRegistrationForm()
    
    data = {
        'form': form,
    }
    
    return render(request, template_name='main/registration.html', context=data) 

def authorization(request): 
    return render(request, template_name='main/authorization.html')