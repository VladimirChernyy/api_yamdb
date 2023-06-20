from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .views import SignUpView, TokenView, UserViewSet
from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'titles', views.TitleViewsSet, basename='title')
router.register(r'categories', views.CategoryViewsSet, basename='category')
router.register(r'genres', views.GenreViewsSet, basename='genre')
# router.register(r'reviews', views.RewiewViewsSet, basename='title')
# router.register(r'comments', views.CommentViewsSet, basename='title')

# urlpatterns =[
#     path('auth/'),
#     path('users/'),
# ]


router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path(
        'v1/auth/signup/',
        SignUpView.as_view({'post': 'create', 'get': 'retrieve'}),
        name='auth-signup'
    ),
    path(
        'v1/auth/token/',
        TokenView.as_view(),
        name='auth-token'
    ),
    path('v1/', include(router.urls)),
]
