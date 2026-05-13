from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PersonalDetails(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    FullName=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    mobile=models.IntegerField(max_length=13)
    email=models.EmailField()
    gitLink=models.CharField(max_length=100)
    linkedIn=models.CharField(max_length=100)
    professionSummary=models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
    

class EductaionDetails(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    course=models.CharField(max_length=100)
    edu_from=models.DateField()
    edu_to=models.DateField()
    
    college=models.CharField(max_length=100)
    cgpa=models.IntegerField(max_length=3)
    
    def __str__(self):
        return self.user.username