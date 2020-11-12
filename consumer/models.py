import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='uploads/', default='uploads/thumbnail.png')
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(null=True)
    visibility=models.BooleanField(default=1)
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(null=True)
    visibility=models.BooleanField(default=1)

class Users(AbstractUser):
    full_names=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    token=models.CharField(max_length=255, null=True)
    url=models.CharField(max_length=255)
    approved=models.BooleanField(default=True)
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(null=True)
    visibility=models.BooleanField(default=1)

class Services(models.Model):
    thumbnail=models.ImageField(upload_to="uploads/services/", default="uploads/thumbnail.png")
    name=models.CharField(max_length=255)
    normal_rate=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    negotiable=models.BooleanField(default=False)
    has_packages=models.BooleanField(default=False)
    url=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(null=True)
    visibility=models.BooleanField(default=1)
    category=models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    user=models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)

class Packages(models.Model):
    condition=models.CharField(max_length=255)
    rate=models.CharField(max_length=255)
    service=models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
    date_added=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateField(null=True)
    visibility=models.BooleanField(default=1)

class Reports(models.Model):
    service=models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
    email=models.CharField(max_length=255)
    details=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    service=models.ForeignKey(Services, null=True, on_delete=models.SET_NULL)
    email=models.CharField(max_length=255)
    comment=models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)

class LoginHistory(models.Model):
    user=models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    device_info=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    current_status=models.BooleanField(default=1)
    time_logged_in=models.DateTimeField(auto_now_add=True)
    time_logged_out=models.DateTimeField(null=True)