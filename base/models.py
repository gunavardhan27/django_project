#from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    semester = models.CharField(max_length=100, null=True)
    
    
class Detail(models.Model):
    course = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100, null=True)
    semester = models.CharField(max_length=100, null=True)

class Subject(models.Model):
    detail = models.ForeignKey(Detail,on_delete=models.CASCADE, null=True)
    s1 = models.CharField(max_length=100, null=True)
    s2 = models.CharField(max_length=100, null=True)
    s3 = models.CharField(max_length=100, null=True)
    s4 = models.CharField(max_length=100, null=True)
    s5 = models.CharField(max_length=100, null=True)
class Mark(models.Model):
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=100, null=True)
    m1 = models.CharField(max_length=100, null=True)
    m2 = models.CharField(max_length=100, null=True)
    m3 = models.CharField(max_length=100, null=True)
    m4 = models.CharField(max_length=100, null=True)
    m5 = models.CharField(max_length=100, null=True)

class Attendance(models.Model):
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    a1 = models.CharField(max_length=100, null=True)
    a2 = models.CharField(max_length=100, null=True)
    a3 = models.CharField(max_length=100, null=True)
    a4 = models.CharField(max_length=100, null=True)
    a5 = models.CharField(max_length=100, null=True)

class Notification(models.Model):
    image = models.ImageField(blank=True)
    data = models.TextField(blank=True)
     