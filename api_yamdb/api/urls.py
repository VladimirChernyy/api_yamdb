from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'titles', views.TitleViewsSet, basename='title')
router.register(r'categories', views.CategoryViewsSet, basename='category')
router.register(r'genres', views.GenreViewsSet, basename='genre')
# router.register(r'reviews', views.RewiewViewsSet, basename='title')
# router.register(r'comments', views.CommentViewsSet, basename='title')

urlpatterns =[
    path('', include(router.urls)),
    # path('auth/'),
    # path('users/'),
]