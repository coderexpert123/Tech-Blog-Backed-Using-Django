from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact= models.CharField(max_length=14)
    email = models.CharField(max_length=114)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
