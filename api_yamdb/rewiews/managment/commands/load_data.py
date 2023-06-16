import csv
import os

from django.core.management.base import BaseCommand


from api_yamdb.settings import LOAD_STATIC_DB
from rewiews.models import Category, Genre, GenreTitle, Title, Comments, Review, Users

CSV_MODELS = {
    'category.csv': Category,
    'comments.csv': Comments,
    'genre.csv': Genre,
    'genre_title.csv': GenreTitle,
    'review.csv': Review,
    'titles.csv': Title,
    'users.csv': Users,
}


class Command(BaseCommand):
    pass






# def load_data(request):
#     for file in os.listdir(LOAD_STATIC_DB)[::-1]:
#         filename = os.path.join(LOAD_STATIC_DB, file)
#         model = CSV_MODELS[file]
#         if os.path.isfile(filename) and file.endswith('.csv'):
#             with open(filename, 'r') as f:
#                 reader = tuple(csv.reader(f))
#                 model.objects.filter(id=reader[[0]]).update_or_create(reader[1:])
