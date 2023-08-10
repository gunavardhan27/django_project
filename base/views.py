from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import User, Mark,Attendance, Notification,Feed
from .forms import UserForm,MyUserCreationForm,Feedback

#from django.contrib.auth import authenticate
#from django.contrib import User

def home(request):
    context = {}
    return render(request, 'base/index.html', context)

def central(request):
    context={}
    return render(request,'base/main_page.html', context)

def login_page(request):
    page='login' 
    context={'page':page}
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password').lower()
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'user doesnt exist')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('main')
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
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('main')
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
    user = User.objects.get(username=request.user)
    form  = UserForm(instance=user)
    if request.method=='POST': 
         form = UserForm(request.POST, request.FILES, instance=user)
         if form.is_valid():
            form.save()
            return redirect('prof')
    context={'form':form}
    return render(request, 'base/admin_page.html',context)

def profile(request):
    user = User.objects.get(username=request.user.username)
    context={'user':user}

    return render(request, 'base/profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'base/passwrd.html', {
        'form': form
    })

def notify(request):
    notes = Notification.objects.all()
    context = {'notes':notes}
    return render(request,'base/notification.html' ,context)

def review(request):
    
    #form = Feedback()
    review = Feed.objects.all()
    form = Feedback()
    if request.method=='POST':
        form = Feedback(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context={'form':form,'review':review}
    return render(request,'base/feedback.html',context)

def edit(request):
    my_form = Feed.objects.get(name=request.user)
    form = Feedback(instance=my_form)
    if request.method=='GET':
        if form.is_valid():
            form.save()
            messages.success(request,'Review updated')
            return redirect('main')
        context = {'form':form}
        return render(request,'base/editfd.html',context)
    else:
        form = Feedback(request.POST,instance=my_form)
        if form.is_valid():
            form.save()
            messages.success(request,'Review updated')
            return redirect('main')
        context = {'form':form}
        return render(request,'base/editfd.html',context)
