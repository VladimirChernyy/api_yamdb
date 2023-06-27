from django.core.validators import (RegexValidator, MaxValueValidator,
                                    MinValueValidator)
from django.db import models
from django.utils import timezone

from api_yamdb.settings import MIN_SCORE, MAX_SCORE
from users.models import User


LENGTH_TEXT = 15


class AbstractDateTimeModel(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} {self.pk}\
            ({self.pub_date.strftime('%Y-%m-%d %H:%M:%S')})"


class Review(AbstractDateTimeModel):
    text = models.TextField(verbose_name='Текст ревью')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор',
    )
    score = models.PositiveIntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(
                MIN_SCORE,
                message='Оценка меньше допустимой',
            ),
            MaxValueValidator(
                MAX_SCORE,
                message='Оценка больше допустимой',
            ),
        ),
    )
    title = models.ForeignKey(
        'Title',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Название произведения',
        null=True,
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


class Comment(AbstractDateTimeModel):
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Aвтор',
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


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(timezone.now().year)])
    description = models.TextField()
    genre = models.ManyToManyField('Genre',
                                   db_index=True,
                                   blank=True, )

    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)

    class Meta:
        ordering = ('-id',)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])

    class Meta:
        ordering = ('-id',)

    def str(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])

    class Meta:
        ordering = ('-id',)

    def str(self):
        return self.name
