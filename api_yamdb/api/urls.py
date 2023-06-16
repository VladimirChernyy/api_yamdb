from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'titles', views.TitleViewsSet, basename='title')
router.register(r'categories', views.CategoryViewsSet, basename='category')
router.register(r'genres', views.GenreViewsSet, basename='genre')
router.register(r'reviews', views.RewiewViewsSet, basename='review')
router.register(r'comments', views.CommentViewsSet, basename='comment')

# urlpatterns =[
#     path('auth/'),
#     path('users/'),
# ]