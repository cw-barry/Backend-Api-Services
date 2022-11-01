from rest_framework import serializers
from blog.models import Post, Comment, Like
from django.db.models import Q

class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'user','post', 'time_stamp', 'content')

        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
            "time_stamp": {"read_only": True},
        }


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    comments = CommentSerializer(many=True, read_only=True)

    has_liked = serializers.SerializerMethodField()
    isowner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id','author', 'category', 'category_id', 'title', 'content', 'image','published_date', 'last_updated', 'slug', 'status', 'comment_count', 'view_count', 'like_count', 'comments', 'has_liked', 'isowner')

        extra_kwargs = {
            "id": {"read_only": True},
            "author": {"read_only": True},
            "published_date": {"read_only": True},
            'last_updated': {"read_only": True},
            'slug': {"read_only": True},
            'comment_count': {"read_only": True}, 
            'view_count': {"read_only": True}, 
            'like_count': {"read_only": True}
        }

    def get_isowner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if obj.author == request.user:
                return True
            return False

    def get_has_liked(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if Post.objects.filter(Q(like__user=request.user) & Q(like__post=obj)).exists():
                return True
            return False

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = [
            "user",
            "post"
        ]