
from django.urls import path
from main.views import UserLogin, UserRegister, UserSignOut, Profile
from main import views

urlpatterns = [
    # If user gos to main page, we need to open the specified files from views.py
    path('', views.home, name='home'), # Call our methon from views.py where we have index() method.
    path('registration/', UserRegister.as_view(), name='registration'), 
    path('authorization/', UserLogin.as_view(), name='authorization'),
    path('signout/', UserSignOut.as_view(), name='sign_out'),
    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    
    # These are previous paths for registration and authentification for user without class-based views:
    # path('my_registration/', views.my_registration, name='my_registration'),
    # path('my_authorization/', views.my_authorization, name='my_authorization'),
]
