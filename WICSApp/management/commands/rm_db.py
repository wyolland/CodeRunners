from django.core.management.base import BaseCommand
from WICSApp.models import Quote

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        Quote.objects.all().delete()

    def handle(self, *args, **options):
        self._create_tags()
