from django.contrib import admin
from . import models

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'original_title',
        'release_date'
    )
    list_display_links = (
        'title',
    )
admin.site.register(models.Movie, MovieAdmin)

class RateAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'movie_title',
        'star',
        'created_at',
        'updated_at'
    )

    def movie_title(self, obj):
        return obj.movie.title
    movie_title.admin_order_field = 'movie'
    movie_title.short_description = 'Movie Title'

admin.site.register(models.Rate, RateAdmin)