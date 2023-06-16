from rest_framework.viewsets import ModelViewSet

from reviews.models import Title, Genre, Category, Review, Comment
from serializers import TitleSerializer, GenreSerializer, CategorySerializer, ReviewSerializer, CommentSerializer


class RewiewViewsSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CommentViewsSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TitleViewsSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewsSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewsSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
