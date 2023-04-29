
from django.urls import path
from . import views # Import our views.py file

urlpatterns = [
    # If user gos to main page, we need to open the specified files from views.py
    path('', views.home), # Call our methon from views.py where we have index() method.
    path('registration/', views.registration,),
    path('authorization/', views.authorization)
]
