import datetime

from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveIntegerField(
        validators=[MaxValueValidator(datetime.datetime.now()
                                      )])
    description = models.TextField()
    genre = models.ManyToManyField('Genre', db_index=True,
                                   blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                regex='^[-a-zA-Z0-9_]+$',
                            )])


class GenreTitle(models.Model):
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)