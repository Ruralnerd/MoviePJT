from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('recommend/', views.movie_recommend, name='movie_recommend'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('genres_list/', views.genres_list, name='genres_list'),
    path('movie_list/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movie_list/<int:movie_pk>/rates/', views.rates_list, name='rates_list'),
    path('rates/<int:rate_pk>/', views.rates_detail, name='rates_detail'),
    path('search/', views.search, name='search'),
]
