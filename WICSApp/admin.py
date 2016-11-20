from django.contrib import admin

from .models import Quote

# Current admin username is "admin", and password is "foobar99"
admin.site.register(Quote)
