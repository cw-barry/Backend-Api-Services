from .models import Post, Like, Comment, PostView
from .serializers import PostSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsOwner
from .pagination import PostPageNumberPagination

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PostPageNumberPagination
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status="p")
    pk_url_kwarg = "slug"
    

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            self.permission_classes = [IsOwner]
        return super(self.__class__, self).get_permissions()
  
    def get_object(self):
        obj = super().get_object()
        if (self.request.user.id):
            PostView.objects.get_or_create(user=self.request.user, post=obj)
        return obj

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

class CommentView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):   
        serializer = self.serializer_class(data=request.data, context={'request': request})
        post = request.data.get('post')
        get_object_or_404(Post, pk=post)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)
        if like_qs.exists():
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)

        data = {
            "messages": "like"
        }
        return Response(data)
