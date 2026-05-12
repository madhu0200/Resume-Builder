from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    first_name=models.TextField(max_length=50)
    last_name= models.TextField(max_length=50)
    email= models.EmailField()
    password=models.TextField(max_length=50)
