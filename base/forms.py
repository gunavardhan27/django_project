from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# model forms are used to create a model form inside website by any user not just the admin
from .models import User,Detail,Subject,Mark,Attendance


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','course','year','semester','password1','password2']



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','name']

