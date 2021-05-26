from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.movie_index, name='movie_index'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_list/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('recommend/', views.movie_recommend, name='movie_recommend'),

    path('recommend/latest_movies/', views.latest_movies, name='latest_movies'),
    
    path('movie_list/<int:movie_pk>/rates/', views.rates_list, name='rates_list'),
    path('rates/<int:rate_pk>/', views.rates_detail, name='rates_detail'),
    path('search/', views.search, name='search'),
]
