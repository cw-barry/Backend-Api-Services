from django.urls import path
from .views import practice_view

urlpatterns = [
    path("<str:file>/", practice_view)
]
