from django.urls import path
from .views import LocationView

urlpatterns = [
    path("search",LocationView.as_view()),
]