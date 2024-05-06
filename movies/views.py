from .models import Movie, Link
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import MovieSerializer, LinkSerializer




class MovieList(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        movie_name = self.request.query_params.get('search')

        if movie_name:
            queryset = queryset.filter(name__icontains=movie_name)
            return queryset[:10]
        
        return queryset


class LinkList(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.select_related('movie').all()
        movie_id = self.request.query_params.get('movie_id')
        movie_name = self.request.query_params.get('movie_name')

        if movie_id:
            queryset = queryset.filter(movie__id=movie_id)
            return queryset[:15]
        
        elif movie_name:
            queryset = queryset.filter(movie__name__icontains=movie_name)
            return queryset[:15]

        else:
            return queryset