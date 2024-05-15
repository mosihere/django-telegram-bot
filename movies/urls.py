from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'movies'


router = DefaultRouter()
router.register('links', views.LinkList, basename='links')
router.register('movies', views.MovieList, basename='movies')

urlpatterns = router.urls
