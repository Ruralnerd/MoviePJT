from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Rate, Genre
from .serializers import GenreSerializer, MovieSerializer, RateSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.core import serializers
from django.http import JsonResponse

from django.db.models import Q

# Create your views here.
def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


def movie_recommend(request):    
    # 최신 영화 10개
    latest_movies = Movie.objects.order_by('-release_date')[:5]
    # 인기 영화 10개
    popular_movies = Movie.objects.order_by('popularity')[:5]
    # 오늘의 영화 추천: vote_count >= 15000, vote_average >= 8.0, 평점 순
    today_movies = Movie.objects.filter(vote_count__gte=15000, vote_average__gte=8.0).order_by('vote_average')[:5]
    # 장르별 영화 추천
    genre = {"액션":28, "모험":12, "애니메이션":16, "코미디":35, "범죄":80, "다큐멘터리":99, "드라마":18, "가족":10751, "판타지":14, "역사":36, "공포":27, "음악":10402, "미스터리":9648, "로맨스":10749, "SF":878, "TV영화":10770, "스릴러":53, "전쟁":10752, "서부":37}

    genre_movies = []

    for key, value in genre.items():
        movie = Movie.objects.filter(genre_ids=value).order_by('-popularity')[:5]
        genre_movies.append([key, movie])

    context = {
        'latest_movies':latest_movies,
        'popular_movies':popular_movies,
        'today_movies':today_movies,
        'genre_movies': genre_movies,
    }
    return render(request, 'movies/recommend.html', context)    


def latest_movies(request): # 최신 영화 5개
    latest = Movie.objects.order_by('-release_date')[:5]
    latest_movies = serializers.serialize('json', latest)
    context = {
        'latest_movies':latest_movies,
    }
    return JsonResponse(context)

def popular_movies(request): # 인기 영화 5개
    popular = Movie.objects.order_by('popularity')[:5]
    popular_movies = serializers.serialize('json', popular)
    context = {
        'popular_movies':popular_movies,
    }
    return JsonResponse(context)

def today_movies(request): # 오늘의 영화 추천 5개: vote_count >= 15000, vote_average >= 8.0, 평점 순
    today = Movie.objects.filter(vote_count__gte=15000, vote_average__gte=8.0).order_by('vote_average')[:5]
    today_movies = serializers.serialize('json', today)    
    context = {
        'today_movies':today_movies,
    }
    return JsonResponse(context)

def genre_movies(request):
    # 장르별 영화 추천
    genre = {"액션":28, "모험":12, "애니메이션":16, "코미디":35, "범죄":80, "다큐멘터리":99, "드라마":18, "가족":10751, "판타지":14, "역사":36, "공포":27, "음악":10402, "미스터리":9648, "로맨스":10749, "SF":878, "TV영화":10770, "스릴러":53, "전쟁":10752, "서부":37}
    genre_movies = []

    for key, value in genre.items():
        movie = Movie.objects.filter(genre_ids=value).order_by('-popularity')[:5]
        genre_movies.append([key, movie])

    genre_movieslist = serializers.serialize('json', genre_movies)
    context = {
        'genre_movieslist':genre_movieslist,
    }
    return JsonResponse(context)   

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rates_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == "GET":
        rates = movie.rate_set.all()
        serializer = RateSerializer(rates, many=True)
        return Response(serializer.data)
    else:
        if request.user.is_authenticated:
            request.data["user"] = request.user.id
            request.data["movie"] = movie.id
            serializer = RateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def rates_detail(request, rate_pk):
    rate = get_object_or_404(Rate, pk=rate_pk)
    if request.method == 'GET':
        serializer = RateSerializer(rate)
        return Response(serializer.data)
    
    else:
        if request.user == rate.user:
            request.data["user"] = request.user.id
            request.data["movie"] = rate.movie.id
            if request.method == 'PUT':
                serializer = RateSerializer(Rate, data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            elif request.method == 'DELETE':
                rate.delete()
                data = {
                    'id': rate_pk,
                    'delete': f'{rate_pk}번 평점이 삭제되었습니다.'
                }
                return Response(data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

def search(request):
    search_movie = request.GET.get('search')
    if search_movie:
        # movies = Movie.objects.filter(Q(title__icontains=search_movie) & Q(original_title__icontains=search_movie) & Q(overview__icontains=search_movie))
        movies = Movie.objects.filter(Q(title__icontains=search_movie))
    context = {
        'movies':movies,
    }    
    return render(request, 'movies/index.html', context)