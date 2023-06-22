from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register(r'titles', views.TitleViewSet, basename='title')
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'genres', views.GenreViewSet, basename='genre')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='title_id')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='review_id')

urlpatterns = [
    path('v1/auth/token/', views.create_token),
    path('v1/auth/signup/', views.create_user),
    path('v1/', include(router.urls)),
]
