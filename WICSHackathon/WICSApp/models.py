from __future__ import unicode_literals

from django.db import models

class Quote(models.Model):
    quote_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
