from django.shortcuts import render
from rest_framework import generics,status
from .models import Student
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your view here.

# class StudentCreateApiView(APIView):
#     def post(self, request, format=None):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'data':serializer.data,'msg':'Recored Inserted Successfully..'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentCreateApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentDestoryApiView(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

class StudentListApiView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['student_name', 'email']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['student_name', 'email']
    filter_backends = [filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['student_name', 'email']
    search_fields = ['student_name', 'email']

class StudentRetrieveApiView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer














