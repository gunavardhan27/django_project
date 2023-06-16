from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import User, Mark,Attendance
from .forms import UserForm,MyUserCreationForm
#from django.contrib.auth import authenticate
#from django.contrib import User

def home(request):
    context = {}
    return render(request, 'base/index.html', context)

def login_page(request):
    page='login' 
    context={'page':page}
    if request.method=="POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user doesnt exist')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'wrong password entered')
    return render(request,'base/login_register.html',context)

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = MyUserCreationForm()
    if request.method=='POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'user already exists')
    context = {'form':form}
    return render(request,'base/login_register.html', context)

def mainpage(request):
    marks = Mark.objects.all()
    context = {'marks':marks}
    return render(request, 'base/student.html', context)

def attendance(request):
    attendance = Attendance.objects.all()
    context = {'attendance':attendance}
    return render(request,'base/attendance.html', context)

def admin_page(request):
    user = User.objects.get(username=request.user.username)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'base/admin_page.html',context)