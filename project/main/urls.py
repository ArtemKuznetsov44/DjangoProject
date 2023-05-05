
from django.urls import path
from . import views # Import our views.py file

urlpatterns = [
    # If user gos to main page, we need to open the specified files from views.py
    path('', views.home, name='home'), # Call our methon from views.py where we have index() method.
    path('my_registration/', views.my_registration, name='my_registration'),
    path('my_authorization/', views.my_authorization, name='my_authorization'),
    path('default_registration/', views.default_registration, name='default_registration'), 
    path('default_authorization/', views.default_authorization, name='default_authorization')
]
