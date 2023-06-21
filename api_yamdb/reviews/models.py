
from datetime import datetime
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    text = models.TextField(verbose_name='Текст ревью')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='Reviews',
        verbose_name='Автор',
    )
    score = models.PositiveIntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(
                1,
                message='Оценка меньше допустимой',
            ),
            MaxValueValidator(
                10,
                message='Оценка больше допустимой',
            ),
        ),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='Reviews',
        verbose_name='Название произведения',
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_review',
            ),
        )

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Aвтор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]

class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.now()
                                      )])
    description = models.TextField()
    genre = models.ManyToManyField('Genre', db_index=True,
                                   blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Comments(models.Model): pass


class Review(models.Model): pass
