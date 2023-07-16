from django.db import models

# Create your models here.

class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=13)
    message = models.CharField(max_length=30)
    

