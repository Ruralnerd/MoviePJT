from rest_framework import serializers
from .models import Genre, Movie, Rate


class RateSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    movie_title = serializers.ReadOnlyField()
    class Meta:
        model = Rate
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    rate = RateSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"