# Generated by Django 3.2 on 2023-06-26 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GenreTitle',
        ),
    ]