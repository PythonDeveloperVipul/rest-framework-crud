from re import S
from django.contrib import admin
from .models import ClassRoom,Student
from django_rest_passwordreset.models import ResetPasswordToken

# Register your models here.
# @admin.register(ClassRoom)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['name']

@admin.register(Student)
class StoreAdmin(admin.ModelAdmin):
    list_display=['classroom','student_name','phone','email','gender','city','state','pincode','address']

admin.site.register(ClassRoom)
admin.site.unregister(ResetPasswordToken)