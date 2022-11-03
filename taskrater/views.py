from django.shortcuts import render
from .models import RateData
from .serializers import RateDataSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import BasePermission
# Create your views here.

class AllowOnlyPost(BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            if request.user.is_staff:
                return True
            return False

        return True

class RateDataView(ListCreateAPIView):
    serializer_class = RateDataSerializer
    queryset = RateData.objects.all()
    permission_classes = [AllowOnlyPost]


