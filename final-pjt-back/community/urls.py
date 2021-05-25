from django.urls import path
from . import views


app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('review/', views.review_list, name='review_list'),
    path('review/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('review/<int:review_pk>/comments/', views.comments_list, name='comments_list'),
    path('comments/<int:comment_pk>/', views.comments_detail, name='comments_detail'),
]