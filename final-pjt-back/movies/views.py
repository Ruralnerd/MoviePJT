from movies.serializers import MovieSerializer
from django.shortcuts import render, redirect, get_object_or_404
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
    words = Movie.objects.all() # 영화 정보 불러오기
    word = request.GET.get('word','') # GET request의 인자 중에 word갑싱 있으면 가져오고, 없으면 빈 문자열 넣기
    if word: # word 값이 있으면
        words = words.filter(title__contains=word)
    return render(request, 'movies/search.html', {'search':words, 'word':word})