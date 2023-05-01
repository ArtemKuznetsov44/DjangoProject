from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(models.Model):
    # verbose_name - this paramets is used for create a humanreadable field name when we will have some erros in our form
    # db_column - this param is userd for create a name for column in database table (when we do not use it, the name in db will be the same as varibale name)

    # First name column:
    first_name = models.CharField(
        verbose_name='first name',
        max_length=16, null=False,
        blank=False,
        db_column='first_name'
    )

    # Midle name column:
    middle_name = models.CharField(
        verbose_name='middle name',
        max_length=16, null=False,
        blank=False,
        db_column='middle_name'
    )

    # Email column:
    email = models.EmailField(
        verbose_name='email adress',
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        db_column='email'
    )

    # Login column:
    login = models.CharField(
        verbose_name='login',
        max_length=12,
        unique=True,
        null=False,
        blank=False,
        db_column='login'
    )

    # Hash password column:
    password = models.CharField(
        verbose_name='password',
        max_length=32,
        null=False,
        blank=False,
        db_column='password'
    )

    # Gender password column:
    gender = models.CharField(
        verbose_name='user gender',
        max_length=6,
        null=False,
        blank=False,
        db_column='gender'
    )

    # Age column:
    age = models.CharField(
        verbose_name='user age',
        max_length=20,
        null=False,
        blank=False,
        db_column='age'
    )

    # To be informed column:
    to_be_informed = models.BooleanField(
        verbose_name='to be informed',
        null=False,
        blank=False,
        db_column='to_be_informed'
    )

    # Registered at column:
    registered_at = models.IntegerField(
        verbose_name='registerd at', 
        null=False, 
        blank=False, 
        db_column='registered_at'
    )
