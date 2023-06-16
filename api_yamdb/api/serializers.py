from rest_framework import serializers

from reviews import models


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Comment


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        models = models.Category
