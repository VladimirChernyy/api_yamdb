from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Display hello'

    def handle(self, *args, **options):
        self.stdout.write('Hello worlds')
