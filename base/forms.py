from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
# model forms are used to create a model form inside website by any user not just the admin
from .models import User,Detail,Subject,Mark,Attendance,Feed


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','course','year','semester','password1','password2']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic','username','name','year','semester']

class Feedback(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['name','rating','review']
