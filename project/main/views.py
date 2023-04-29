from django.shortcuts import render
# from django.http import HttpResponse # This class is used for generate HTTP-fromat responses (answers)

# Create your views here.

# To my mind it is like an action in Yii (maybe it is a worse statment)
# The request param is required (обязетельный):
def home(request): 
    # return HttpResponse("<h1>Main page</h1>")
    return render(request, template_name='main/home.html')
    # Do nothing:
    # pass
    
def registration(request): 
    return render(request, template_name='main/registration.html') 

def authorization(request): 
    return render(request, template_name='main/authorization.html')