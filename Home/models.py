from django.db import models

# Create your models here.

class UserDetails(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    key = models.CharField(max_length=100, default=" ")
