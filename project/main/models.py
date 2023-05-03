from django.db import models


# Create your models here.
# This is a model class which is used as a database table with the same name and fields:

class User(models.Model):
    first_name = models.CharField(max_length=16, blank=False, null=False)
    middle_name = models.CharField(max_length=16, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False, unique=True)
    login = models.CharField(max_length=12, blank=False, null=False, unique=True)
    password = models.CharField(max_length=16, blank=False, null=False)
    gender = models.CharField(max_length=6, choices=[("woman", "Woman"), ("man", 'Man')], blank=False, null=False)
    age = models.CharField(max_length=20,
                           choices=[('under_18', 'Under 18 years old'), ('over_18', 'Over 18 years old')], blank=False,
                           null=False)
    to_be_informed = models.BooleanField(default=False)
    # auto_now_add - it is a param which says that this field will get the DataTime value automatically and such
    # value in database you can't to update unlike of usage auto_now param
    reg_at = models.DateTimeField(auto_now_add=True)
