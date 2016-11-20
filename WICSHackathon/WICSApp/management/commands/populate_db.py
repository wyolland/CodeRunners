from django.core.management.base import BaseCommand
from WICSApp.models import Quote
import datetime
from django.utils import timezone

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
        file_url = "input.txt"
        with open(file_url) as f:
            for line in f:
                inner_list = [elt.strip() for elt in line.split(',')]
                to_append = str(inner_list)[2:len(str(inner_list))-2]
                to_append = to_append.lower()
                new_string = to_append[0].upper()
                to_append = new_string + to_append[1:]
                print(to_append)
                date_now = datetime.datetime.now()
                date_now = timezone.make_aware(date_now, timezone.get_current_timezone())

                the_quote = Quote(quote_text=to_append, pub_date=date_now, rank=0)
                the_quote.save()

    def handle(self, *args, **options):
        self._create_tags()
