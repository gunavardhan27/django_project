from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.login_page,name="login_reg"),
    path('logout/',views.logout_user,name="log_out"),
    path('register/',views.register_user,name="register"),
    path('student/', views.mainpage, name="stud"),
    path('att/',views.attendance,name="at"),
    path('create/',views.admin_page,name='admin')
]