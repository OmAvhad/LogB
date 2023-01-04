from rest_framework import serializers
from .models import Blogs, Comments, Likes


class BlogsSerializer(serializers.Serializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class CommentsSerializer(serializers.Serializer):
    class Meta:
        model = Comments
        fields = '__all__'


class LikesSerializer(serializers.Serializer):
    class Meta:
        model = Likes
        fields = '__all__'
