from rest_framework import serializers
# from rest_framework.fields import ReadOnlyField
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y.%m.%d %H:%M')
    updated_at = serializers.DateTimeField(format='%Y.%m.%d %H:%M')

    class Meta:
        model = Comment
        fields = "__all__"


class ReviewListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    created_at = serializers.DateTimeField(format='%Y.%m.%d %H:%M')
    class Meta:
        model = Review
        fields = ('id', 'title', 'created_at', 'movie_title', 'content', 'comment_count')


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    created_at = serializers.DateTimeField(format='%Y.%m.%d %H:%M')
    updated_at = serializers.DateTimeField(format='%Y.%m.%d %H:%M')
    
    class Meta:
        model = Review
        fields = "__all__"