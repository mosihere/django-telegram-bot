from .models import Movie, Link
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import MovieSerializer, LinkSerializer




class MovieList(ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.values('id', 'name', 'published_at', 'poster_url')
        movie_name = self.request.query_params.get('search')

        if movie_name:
            queryset = queryset.filter(name__icontains=movie_name).order_by('-published_at')
            return queryset[:10]
        
        return queryset


class LinkList(ReadOnlyModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        queryset = Link.objects.values('id', 'link', 'quality', 'codec', 'movie__name', 'movie__published_at')
        movie_id = self.request.query_params.get('movie_id')

        if movie_id:
            queryset = queryset.filter(movie__id=movie_id)
            return queryset[:20]
        
        return queryset