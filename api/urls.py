from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('StudentCreateApiView/',views.StudentCreateApiView.as_view()),
    path('StudentUpdateApiView/<int:pk>/',views.StudentUpdateApiView.as_view()),
    path('StudentDestoryApiView/<int:pk>/',views.StudentDestoryApiView.as_view()),
    path('StudentListApiView/',views.StudentListApiView.as_view()),
    path('StudentRetrieveApiView/<int:pk>/',views.StudentRetrieveApiView.as_view()),
    
]
