from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, ListView
# from .models import MyRegisteredUser - This is not for use now.

# The default model for Users in Django:
from django.contrib.auth.models import User
from main.models import Post
# Import our forms from file (all out forms are based on default Django forms)
from main.forms import RegisterUserForm, LoginUserForm, AddPost

# To my mind it is like an action in Yii (maybe it is a worse statement)
# The request param is required (обязетельный):
def home(request): 
    # return HttpResponse("<h1>Main page</h1>")
    return render(request, template_name='main/home.html')
    # Do nothing:
    # pass
    
''' My previous functions for registration and authentification:
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
'''

''' Using a default model for registration but without class-based view:
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
'''
# This is a class-based view - CreateView - 
# View for creating a new object, with a response rendered by a template.
class UserRegister(CreateView):
    model = User
    template_name = "main/registration.html"
    form_class = RegisterUserForm
    
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('home')
    
class UserLogin(LoginView): 
    # Using form for authentification:
    form_class = LoginUserForm
    # Template name for this form:
    template_name = "main/authorization.html"
   
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('home')
    
    
class UserSignOut(LogoutView):
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        return reverse_lazy('home')
 
    
class Profile(DetailView):
    model = User
    template_name='main/user_info.html'
    # This var now can be use in our templates:
    context_object_name = 'user'


class ShowPosts(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='main/home.html'
   
    
class AddNewPost(CreateView): 
    form_class = AddPost
    template_name = 'main/add_post.html'
    
    # This method is called when all form field are valid:
    def form_valid(self, form):
        # Здесь происход обращение к сущности формы, которая связана с моделью Post, 
        # в которой есть поле user (внешний ключ), который необходимо заполнить id пользователя. 
        # Данный id пользователя мы берем ис самого запроса. 
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self): 
        return reverse_lazy('home')