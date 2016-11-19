from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # needed to support Python 2
class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.quote_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
