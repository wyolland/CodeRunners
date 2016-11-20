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
                print(to_append)
                # in alternative, if you need to use the file content as numbers
                # inner_list = [int(elt.strip()) for elt in line.split(',')]
                date_now = datetime.datetime.now()
                date_now = timezone.make_aware(date_now, timezone.get_current_timezone())

                the_quote = Quote(quote_text=to_append, pub_date=date_now)
                the_quote.save()

    def handle(self, *args, **options):
        self._create_tags()
