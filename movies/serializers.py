from rest_framework import serializers
from .models import Movie, Link




        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'published_at', 'poster_url']        


class SimpleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'published_at']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'link', 'quality', 'codec', 'movie']
        
    movie = SimpleMovieSerializer()