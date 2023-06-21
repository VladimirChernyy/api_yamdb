import csv
import os

from django.core.management.base import BaseCommand


from api_yamdb.settings import LOAD_STATIC_DB
from reviews.models import Category, Genre, GenreTitle, Title, Comments, Review
from users.models import User

CSV_MODELS = {
    'category.csv': Category,
    #'comments.csv': Comments,
    'genre.csv': Genre,
    'genre_title.csv': GenreTitle,
    #'review.csv': Review,
    'titles.csv': Title,
    'users.csv': User,
}
CSV_MODELS_ID = {
    'category': ('category', Category),
    'title_id': ('title', Title),
    'genre_id': ('genre', Genre),
    'author': ('author', User),
    #'review_id': ('review', Review),
}


def open_csv_file(file_name):
    csv_file = file_name
    csv_path = os.path.join(LOAD_STATIC_DB, csv_file)
    with open(csv_path) as file:
        return list(csv.reader(file))


def change_foreign_values(data_csv):
    data_csv_copy = data_csv.copy()
    for field_key, field_value in data_csv.items():
        if field_key in CSV_MODELS_ID.keys():
            field_key0 = CSV_MODELS_ID[field_key][0]
            data_csv_copy[field_key0] = CSV_MODELS_ID[field_key][
                1].objects.get(
                pk=field_value)
    return data_csv_copy


def load_csv(file_name, class_name):
    data = open_csv_file(file_name)
    rows = data[1:]
    for row in rows:
        data_csv = dict(zip(data[0], row))
        data_csv = change_foreign_values(data_csv)
        table = class_name(**data_csv)
        table.save()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for key, value in CSV_MODELS.items():
            load_csv(key, value)
