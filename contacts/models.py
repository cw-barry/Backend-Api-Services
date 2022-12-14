from django.db import models

# Create your models here.

class Contact(models.Model):
    gender_choices= [("F",'Female'), ("M", 'Male'),('O','Other')]
    username = models.CharField(max_length=30,unique=True)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    gender = models.CharField(max_length=1,choices=gender_choices)

    def __str__(self):
        return f"{self.username}"
    