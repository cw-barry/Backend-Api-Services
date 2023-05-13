from django.shortcuts import render, HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Todo API</h1>")

@api_view(["GET"])
def TodoList(request):
    queryset = Todo.objects.all()
    serializer = TodoSerializer(queryset, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def todo_add(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(["GET","POST"])
def todo_list_add(request):
    if request.method == "GET":
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many = True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

@api_view(["GET","PUT","PATCH","DELETE"])
def todo_detail(request, pk):
    qs = Todo.objects.get(pk = pk)
    if request.method == "GET":
        serializer = TodoSerializer(qs)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TodoSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "PATCH":
        serializer = TodoSerializer(instance=qs,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    elif request.method == "DELETE":
        qs.delete()
        return Response({"message" : "deleted successfully"})

class TodoListCreate(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user = self.request.user)

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoAllOperations(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
