from django.shortcuts import render, get_object_or_404
from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer, DepartmentDetailSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User

class DepartmentView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]


class DepartmentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminOrReadOnly]

    lookup_field = "name__iexact"
    # lookup_field = "name" # default is "pk"
    lookup_url_kwarg = "departmentname"

    # get the single record from our database
    # def get_object(self):
    #     depname = self.kwargs.get("departmentname")
    #     # obj = Department.objects.get(name__iexact = depname)
    #     obj = get_object_or_404(Department, name__iexact = depname)
    #     return obj

    # if you want to change your serializer dynamically, this is the method
    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.request.user.is_staff:
            person = Personnel.objects.get(email = self.request.user.email)
            depname = self.kwargs.get("departmentname")
            print(depname)
            print(person.department.name)
            print(self.request.user.__dict__)
            if person.department.name.lower() == depname.lower():
                serializer = DepartmentDetailSerializer

        return serializer

   

class PersonnelView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class PersonnelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
