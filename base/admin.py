from django.contrib import admin
from .models import User,Detail,Mark,Subject,Attendance
# Register your models here.
admin.site.register(User)
admin.site.register(Detail)
admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(Attendance)
