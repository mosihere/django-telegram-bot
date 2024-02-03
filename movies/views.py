from django.shortcuts import render
from .models import Movie, Link
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import MovieSerializer, LinkSerializer




class MovieList(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class LinkList(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.all()
        movie_name = self.request.query_params.get('movie_name')
        if movie_name:
            new_queryset = queryset.filter(movie__name__iexact=movie_name)
            print(new_queryset.exists())

        if new_queryset.exists():
            return new_queryset
        
        else:
            queryset = queryset.filter(movie__name__icontains=movie_name)
            print(queryset.exists())

        return queryset