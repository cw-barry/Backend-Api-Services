from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer, UserSerializer, CustomTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from .signals import *

# Create your views here.

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {}
        if Token.objects.filter(user=user).exists():
            token = Token.objects.get(user=user)
            data['key'] = token.key
        else:
            data['error'] = 'User dont have token. Please login'
        data['user'] = serializer.data
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     data = serializer.data

    #     token = Token.objects.get(user=user)
    #     data["token"] = token.key

    #     headers = self.get_success_headers(serializer.data)
    #     return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()


# class ListUserView(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         data = [[user.username, user.password] for user in User.objects.all()]
#         return Response(data)