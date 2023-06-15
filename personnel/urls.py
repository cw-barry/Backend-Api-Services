from .views import *
from django.urls import path

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    # path("department/<int:pk>/", DepartmentDetailView.as_view()),
    path("department/<str:departmentname>/", DepartmentDetailView.as_view()),
    path("personnel/", PersonnelView.as_view()),
    path("personnel/<int:pk>/", PersonnelDetailView.as_view()),
]