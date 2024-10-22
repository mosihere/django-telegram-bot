from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


app_name = 'movies'


router = DefaultRouter()
router.register('links', views.LinkViewSet, basename='link')
router.register('movies', views.MovieViewSet, basename='movie')
router.register('users', views.UserViewSet, basename='user')
router.register('user-searches', views.UserSearchViewSet, basename='usersearch')

urlpatterns = router.urls
