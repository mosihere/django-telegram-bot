from .models import Movie, Link, User, UserSearch
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer, LinkSerializer, UserSerializer, UserSearchSerializer
from .throttling import MovieLinkThrottle, MovieSearchThrottle



class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    throttle_classes = [MovieSearchThrottle]

    def get_queryset(self):
        queryset = Movie.objects.only('id', 'name', 'published_at', 'poster_url', 'subtitle_url')
        movie_name = self.request.query_params.get('search')

        if movie_name:
            queryset = queryset.filter(name__icontains=movie_name).order_by('-published_at')
            return queryset[:10]
        
        return queryset


class LinkViewSet(ModelViewSet):
    serializer_class = LinkSerializer
    throttle_classes = [MovieLinkThrottle]
    
    def get_queryset(self):
        queryset = Link.objects.select_related('movie').only('id', 'link', 'quality', 'codec','movie__name', 'movie__published_at', 'movie__subtitle_url')
        movie_id = self.request.query_params.get('movie_id')

        if movie_id:
            queryset = queryset.filter(movie__id=movie_id)
            return queryset[:20]
        
        return queryset


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserSearchViewSet(ModelViewSet):
    serializer_class = UserSearchSerializer
    queryset = UserSearch.objects.select_related('user').all()