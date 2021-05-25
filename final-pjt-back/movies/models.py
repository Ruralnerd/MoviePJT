from datetime import datetime
from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    adult = models.BooleanField()
    genre_ids = models.ManyToManyField(Genre)
    original_language = models.TextField(blank=True)
    original_title = models.TextField(blank=True)
    title = models.CharField(max_length=150)
    overview = models.TextField(blank=True)
    popularity = models.FloatField(blank=True)
    poster_path = models.CharField(max_length=255, blank=True)
    release_date = models.DateField(blank=True)
    vote_average = models.FloatField(blank=True)
    vote_count = models.IntegerField(blank=True)
    
class Rate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.IntegerField()
    opinion = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
