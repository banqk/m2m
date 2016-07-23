from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hedge_instrument.views',
    url(r'hedge_inst/$', 'hedge_inst'),
    url(r'create_inst/$', 'create_inst'),
    url(r'remove_inst/$', 'remove_inst'),
    url(r'update_inst/$', 'update_inst'),
)
