from rest_framework.viewsets import ModelViewSet

from rewiews.models import Title, Genre, Category
from .serializers import TitleSerializer, GenreSerializer, CotegorySerializer


class TitleViewsSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewsSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CotegorySerializer


class GenreViewsSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


