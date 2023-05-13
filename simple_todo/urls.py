from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api", TodoAllOperations)


urlpatterns = [
    # path('', todo_list_add),
    # path("<int:pk>/", todo_detail),
    # path("list/", TodoList),
    # path("add/", todo_add),

    path("", TodoListCreate.as_view()),
    path("<int:pk>/", TodoDetail.as_view()),
] + router.urls
