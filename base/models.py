#from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(null=True, default="Education Logo.png")
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
    def __str__(self):
        return f"{self.detail.course}-{self.detail.year}-{self.detail.semester}"


class Mark(models.Model):
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(max_length=100, null=True)
    m1 = models.CharField(max_length=100, null=True)
    m2 = models.CharField(max_length=100, null=True)
    m3 = models.CharField(max_length=100, null=True)
    m4 = models.CharField(max_length=100, null=True)
    m5 = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return f"{self.student_id}-{self.subjects.detail.year}-{self.subjects.detail.semester}"


class Attendance(models.Model):
    subjects = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    a1 = models.CharField(max_length=100, null=True)
    a2 = models.CharField(max_length=100, null=True)
    a3 = models.CharField(max_length=100, null=True)
    a4 = models.CharField(max_length=100, null=True)
    a5 = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return f"{self.user.username}-{self.subjects.detail.year}-{self.subjects.detail.semester}"

class Notification(models.Model):
    image = models.ImageField(blank=True)
    data = models.TextField(blank=True)
     
class Feed(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    rating = models.PositiveIntegerField(null=True)
    review = models.TextField(max_length=200, null=True)
