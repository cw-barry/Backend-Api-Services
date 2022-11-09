from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwner
# Create your views here.

class TodoView(ModelViewSet):
    # permission_classes = [IsAuthenticated, IsOwner]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         return super().get_queryset()
    #     else:
    #         return Todo.objects.filter(user = self.request.user)