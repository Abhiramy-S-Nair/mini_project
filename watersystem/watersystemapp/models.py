from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    firstname = models.TextField(max_length=100, default="")
    lastname = models.TextField(max_length=100, default="")
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=128, default="")
   
   

    def __str__(self):
        return self.password