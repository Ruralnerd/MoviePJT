from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Rate, Genre
from .serializers import GenreSerializer, MovieSerializer, RateSerializer

# Create your views here.
def movie_index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def movie_recommend(request):
    genres = {28:"액션", 12:"모험", 16:"애니메이션", 35:"코미디", 80:"범죄", 99:"다큐멘터리", 18:"드라마", 10751:"가족", 14:"판타지", 36:"역사", 27:"공포", 10402:"음악", 9648:"미스터리", , 10749:"로맨스", 878:"SF", 10770:"TV영화", 53:"스릴러", 10752:"전쟁", 37:"서부"}
    # 최신 영화 100개
    latest_movie = Movie.objects.order_by('-release_date')[:100]
    # 인기 영화 100개
    popular_movie = Movie.objects.order_by('popularity')[:100]
    # runtime 120분 이상, 최신순 
    runtime_movie = Movie.objects.filter(runtime__gte=120).order_by('-release_date')
    # 추천 영화 : vote_count >= 15000, vote_average >= 8.0, 평점 순
    today_movie = Movie.objects.filter(vote_count__gte=15000, vote_average__gte=8.0).order_by('vote_average')

    context = {
        'latest_movie':latest_movie,
        'popular_movie':popular_movie,
        'runtime_movie':runtime_movie,
        'today_movie':today_movie,
    }
    return render(request, 'movies/recommend.html', context)





@api_view(['GET'])
def genres_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genres_detail(request, genres_pk):
    genre = get_object_or_404(Genre, pk=genres_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

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

@api_view(['GET', 'POST'])
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
    word = request.GET.get('word','') # GET request의 인자 중에 word값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if word: # word 값이 있으면
        movies = Movie.objects.filter(Q(title__contains=word) | Q(original_title__contains=word))
    else:
        movies = '일치하는 검색 결과가 없습니다.'
    context = {
        'word': word,
        'movies': movie,
    }
    return render(request, 'movies/search.html', context)
