from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register(r'titles', views.TitleViewsSet, basename='title')
router.register(r'categories', views.CategoryViewsSet, basename='category')
router.register(r'genres', views.GenreViewsSet, basename='genre')
# router.register(r'reviews', views.RewiewViewsSet, basename='title')
# router.register(r'comments', views.CommentViewsSet, basename='title')



urlpatterns = [
    path(
        'v1/auth/signup/',
        views.SignUpView.as_view({'post': 'create', 'get': 'retrieve'}),
        name='auth-signup'
    ),
    path(
        'v1/auth/token/',
        views.TokenView.as_view(),
        name='auth-token'
    ),
    path('v1/', include(router.urls)),
]
