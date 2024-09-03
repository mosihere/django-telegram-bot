from django.db import models




class Movie(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255)
    published_at = models.IntegerField(blank=True, null=True)
    poster_url = models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name', 'poster_url'])
        ]


class Link(models.Model):
    link = models.CharField(max_length=255)
    quality = models.CharField(max_length=10)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='links')
    codec = models.CharField(max_length=4)
