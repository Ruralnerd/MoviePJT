from rest_framework import serializers
# from rest_framework.fields import ReadOnlyField
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = "__all__"


class ReviewListSerializer(serializers.ModelSerializer):
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    username = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = ('id', 'title', 'username', 'created_at', 'movie_title', 'content', 'comment_count')


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    
    class Meta:
        model = Review
        fields = "__all__"