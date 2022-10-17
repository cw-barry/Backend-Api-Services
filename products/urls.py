from django.urls import path
from rest_framework import routers
from .views import CategoryView, ProductView, bulk_create_api

router = routers.DefaultRouter()
router.register('category', CategoryView)
router.register('', ProductView)

urlpatterns = [
    path('bulk/', bulk_create_api)

]

urlpatterns += router.urls