from rest_framework import serializers

from rewiews import models


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Genre


class CotegorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Category
