from rest_framework import serializers
from .models import User, UserSearch, Link, Movie


        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'url', 'poster_url', 'subtitle_url', 'trailer_url']
        read_only_fields = ['id']


class LinkSerializer(serializers.ModelSerializer):
    movie_name = serializers.SerializerMethodField()
    movie_published_at = serializers.SerializerMethodField()
    movie_subtitle_url = serializers.SerializerMethodField()
    movie_trailer_url = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'link', 'quality', 'codec', 'movie_name', 'movie_published_at', 'movie_subtitle_url', 'movie_trailer_url']
        read_only_fields = ['id']

    def get_movie_name(self, obj):
        return obj.movie.name

    def get_movie_published_at(self, obj):
        return obj.movie.published_at

    def get_movie_subtitle_url(self, obj):
        return obj.movie.subtitle_url

    def get_movie_trailer_url(self, obj):
        return obj.movie.trailer_url


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' ,'telegram_id', 'username', 'first_name', 'last_name', 'created_at', 'last_use']
        read_only_fields = ['id', 'created_at']


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearch
        fields = ['id' ,'user', 'query', 'timestamp']
        read_only_fields = ['id', 'timestamp']