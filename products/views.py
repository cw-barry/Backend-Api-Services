from rest_framework.viewsets import ModelViewSet
from .models import Category, Products
from .serializers import CategorySerializer, ProductsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadonly

# Create your views here.
class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrReadonly]

class ProductView(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAdminOrReadonly]