from rest_framework.viewsets import ModelViewSet
from .models import Category, Products
from .serializers import CategorySerializer, ProductsSerializer, BulkProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadonly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadonly]

class ProductView(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAdminOrReadonly]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields=['title']
    filterset_fields = ['category']

@api_view(['POST'])
def bulk_create_api(request):
    serializer = BulkProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
    