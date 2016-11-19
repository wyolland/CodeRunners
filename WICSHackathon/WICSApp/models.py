from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Makes shit work for python 2
@python_2_unicode_compatible

class Quote(models.Model):
    # A field in our database
    quote_text = models.CharField(max_length=200)

    # It's important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects' representations are used throughout Django's automatically-generated admin.
    def __str__(self):
        return self.quote_text
