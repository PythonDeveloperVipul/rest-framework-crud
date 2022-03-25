from rest_framework import serializers
from .models import ClassRoom,Student
# Create your serializer here.

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['classroom','student_name','phone','email','gender','city','state','pincode','address']

class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassRoom
        fields="__all__"

