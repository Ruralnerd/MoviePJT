from django.contrib import admin
from . import models

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'title',
        'movie_title',
        'created_at',
        'updated_at'
    )

admin.site.register(models.Review, ReviewAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'review_title',
        'content',
        'created_at',
        'updated_at'
    )

    def review_title(self, obj):
        return obj.review.title
    review_title.admin_order_field = 'review'
    review_title.short_description = 'Review Title'

admin.site.register(models.Comment, CommentAdmin)
