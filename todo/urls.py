from django.urls import path
from rest_framework import routers
from .views import TodoView

router = routers.DefaultRouter()
router.register('', TodoView)

urlpatterns = [
] + router.urls
