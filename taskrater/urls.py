from django.urls import path
from .views import RateDataView

urlpatterns = [
    path("",RateDataView.as_view())
]
