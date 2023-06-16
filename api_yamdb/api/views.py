from rest_framework.viewsets import ModelViewSet
from rewiews.models import Category, Genre, Title
from serializers import CotegorySerializer, GenreSerializer, TitleSerializer


class TitleViewsSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CategoryViewsSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CotegorySerializer


class GenreViewsSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


