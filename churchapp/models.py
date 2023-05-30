# type:ignore
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    def __str__(self):
        return self.username

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='admin')
    name = models.CharField(max_length=30,blank=False,default='name')
    
    def __str__(self):
        return f'{self.user.username} admin'

class Client(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True,related_name='client')
   name = models.CharField(max_length=30,blank=False,default='name')
    
   def __str__(self):
       return f'{self.user.username} client'
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=255, default="Add Bio....", blank=True)
    name = models.CharField(max_length=60,blank=True)
    location = models.CharField(max_length=60,blank=True)
    profile_pic= CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username} profile'