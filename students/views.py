from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class StudentView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
