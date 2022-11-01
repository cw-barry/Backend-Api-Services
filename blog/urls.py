from django.urls import path
from rest_framework import routers
from .views import PostViewSet, CommentView, LikeView

router = routers.DefaultRouter()
router.register('', PostViewSet)

urlpatterns = [

    path("comment/", CommentView.as_view(), name="comment"),
    path("like/<str:slug>/", LikeView.as_view(), name="like"),

] + router.urls
