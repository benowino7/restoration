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

class Cermon(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    theme = models.CharField(max_length=150)
    reading = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')
    date = models.CharField(max_length=100,default="YYYY-MM-DD")
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.theme} theme'

    
class Review(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = CloudinaryField('image')
    comment = models.TextField(max_length=300,default=' add a comment')
    def __str__(self):
        return f'{self.first_name}'


class ImpactCategory(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    

class Impact(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ImpactCategory,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    image = CloudinaryField('image')
    def __str__(self):
        return f'{self.title}'


class Event(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = CloudinaryField('image')
    event_date = models.CharField(max_length=100, default='DD-MM-YYYY')
    def __str__(self):
        return f'{self.title}'
    
class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    method =models.CharField(max_length=100)
    paybill = models.IntegerField(blank=True,null=True)
    till = models.IntegerField(blank=True,null=True)
    account = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(max_length=255,null=True,blank=True)
    def __str__(self):
        return f'{self.method}'

