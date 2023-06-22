from django_filters.rest_framework import FilterSet, CharFilter

from reviews.models import Title


class TitleFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains')
    category = CharFilter(
        field_name='category__slug',
        lookup_expr='exact'
    )
    genre = CharFilter(field_name='genre__slug', lookup_expr='exact')

    class Meta:
        model = Title
        fields = ['name', 'category', 'genre', 'year']
