from rest_framework import serializers



        
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    published_at = serializers.IntegerField()
    poster_url = serializers.CharField(max_length=255)
    subtitle_url = serializers.CharField(max_length=255)


class LinkSerializer(serializers.Serializer):   
    id = serializers.IntegerField()
    link = serializers.CharField(max_length=255)
    quality = serializers.CharField(max_length=10)
    codec = serializers.CharField(max_length=4)
    name = serializers.CharField(source='movie__name')
    published_at = serializers.IntegerField(source='movie__published_at')
    subtitle_url = serializers.CharField(max_length=255, source='movie__subtitle_url')