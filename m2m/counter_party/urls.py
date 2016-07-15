from django.conf.urls import patterns, url

urlpatterns = patterns(
    'counter_party.views',
    url(r'counters/$', 'counters'),
    url(r'create_counter/$', 'create_counter'),
    url(r'remove_counter/$', 'remove_counter'),
    url(r'update_counter/$', 'update_counter'),
)
