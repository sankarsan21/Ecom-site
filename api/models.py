from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50,default='Anonymous')
    email = models.EmailField(max_length=250,unique=True)

    username=None

    USERNAMEFIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=10,blank = True, null = True)
    gender = models.CharField(max_length=10,blank = True,null = True)

    session_Token = models.CharField(max_length=10,default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
