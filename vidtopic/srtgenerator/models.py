from distutils.command.upload import upload
from django import forms
from django.db import models

# Create your models here.

class UserFiles(models.Model):
    
    file = models.FileField()
    title = models.CharField(max_length=100, null=True)