import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.generics import get_object_or_404

from reviews.models import Title, Genre, Category, Review, Comment
from users.models import User


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=CurrentUserDefault(), slug_field="username", read_only=True
    )

    def validate(self, data):
        request = self.context["request"]
        if request.method == "POST":
            author = request.user
            title_id = self.context["view"].kwargs.get("title_id")
            title = get_object_or_404(Title, pk=title_id)
            if Review.objects.filter(title=title, author=author).exists():
                raise ValidationError("Нельзя добавить больше 1 комментария")
        return data

    class Meta:
        fields = ("id", "text", "author", "score", "pub_date", "title")
        model = Review
        read_only_fields = ("title",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Comment
        read_only_fields = ("review",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = serializers.IntegerField(read_only=True, required=False)

    class Meta:
        fields = '__all__'
        model = Title


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class CreateUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, username):
        if username.lower() == 'me':
            raise serializers.ValidationError(
                "Использовать имя 'me' в качестве username запрещено!"
            )
        if not re.search(r'[a-zA-Z][a-zA-Z0-9-_/.]{1,20}$', username):
            raise ValidationError('Недопустимые символы в имени')
        return username

    def validate(self, data):
        username = data['username']
        email = data['email']
        if User.objects.filter(username=username, email=email).exists():
            return data
        if User.objects.filter(username=username).exists():
            raise ValidationError('Имя уже занято')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Почта уже занята')
        return data


class CreateTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code',)
