from django.conf.urls import url

import views

urlpatterns = [
    # ex: /WICSApp/
    url(r'^$', views.index, name='index'),
    # ex: /WICSApp/5/
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /WICSApp/5/results/
    url(r'^(?P<quote_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /WICSApp/5/vote/
    url(r'^(?P<quote_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
