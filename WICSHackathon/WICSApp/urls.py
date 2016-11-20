
from django.conf.urls import url

import views

urlpatterns = [
    # ex: /WICSApp/
    url(r'^$', views.index, name='index'),
    # ex: /WICSApp/5/
    url(r'^(?P<quote_id>[0-9]+)/$', views.upvote, name='upvote'),
    # ex: /WICSApp/5/results/
    url(r'^(?P<quote_id>[0-9]+)/results/$', views.downvote, name='downvote'),
    # ex: /WICSApp/5/vote/
    url(r'^(?P<quote_id>[0-9]+)/random/$', views.random, name='random'),
]
