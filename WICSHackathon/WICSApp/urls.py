#URL confs go REGEX -> WEBADDRESS
from django.conf.urls import url

from . import views

urlpatterns = [
    # RegEx anything
    
    # ex: /WICSApp/
    url(r'^$', views.index, name='index'),

    # ex: /WICSApp/5/
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
]
