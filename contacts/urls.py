
from django.urls import path
from .views import ContactList, ContactRUD

urlpatterns = [
    path('', ContactList.as_view(), name='list'),
    path('<int:pk>/', ContactRUD.as_view(), name='detail')
]
