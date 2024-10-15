from rest_framework.viewsets import ModelViewSet
from .models import Category, Products
from .serializers import ProductCategorySerializer, ProductsSerializer, BulkProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadonly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class CategoryView(ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadonly]

class CustomPagination(PageNumberPagination):
    # page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Query parameter to specify the number of items per page
    max_page_size = 500  # Maximum page size limit

class ProductView(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # permission_classes = [IsAdminOrReadonly]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ['title']
    filterset_fields = ['category']
    pagination_class = CustomPagination  # Use the custom pagination class

    # def list(self, request, *args, **kwargs):
    #     # Call the original list method
    #     response = super().list(request, *args, **kwargs)
    #     return Response(response.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def bulk_create_api(request):
    serializer = BulkProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)
    