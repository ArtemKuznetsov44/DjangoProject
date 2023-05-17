from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# This is a model class which is used as a database table with the same name and fields:
'''
class MyRegisteredUser(models.Model):
    first_name = models.CharField(max_length=16, blank=False, null=False)
    middle_name = models.CharField(max_length=16, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False, unique=True)
    login = models.CharField(max_length=12, blank=False, null=False, unique=True)
    password = models.CharField(max_length=32, blank=False, null=False)
    gender = models.CharField(max_length=6, choices=[("woman", "Woman"), ("man", 'Man')], blank=False, null=False)
    age = models.CharField(max_length=20,
                           choices=[('under_18', 'Under 18 years old'), ('over_18', 'Over 18 years old')], blank=False,
                           null=False)
    to_be_informed = models.BooleanField(default=False)
    # auto_now_add - it is a param which says that this field will get the DataTime value automatically and such
    # value in database you can't to update unlike of usage auto_now param
    reg_at = models.DateTimeField(auto_now_add=True)
''' 

class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    content = models.TextField(blank=False, null=False)
    time_created = models.DateField(auto_now_add=True)
    time_updated = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # This method is useful when we whant to get our records. We will see titles of posts instead of Id:
    def __str__(self):
        return self.title

    # This method is useful for making a dinamic url adress:
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
