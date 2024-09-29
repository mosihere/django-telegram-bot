from django.db import models




class Movie(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    published_at = models.IntegerField(blank=True, null=True)
    trending = models.BooleanField(default=False)
    poster_url = models.CharField(max_length=255, null=True)
    subtitle_url = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Link(models.Model):
    link = models.CharField(max_length=255, unique=True)
    quality = models.CharField(max_length=10)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='links')
    codec = models.CharField(max_length=4)


class User(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_use = models.DateTimeField(auto_now=True)


class UserSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)