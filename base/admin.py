from django.contrib import admin
from .models import User,Detail,Mark,Subject,Attendance,Notification
# Register your models here.

class Show(admin.ModelAdmin):
    list_display = ("course","year","semester")


admin.site.register(User)
admin.site.register(Detail, Show)
admin.site.register(Mark)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(Notification)
