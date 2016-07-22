from django.conf.urls import patterns, url

urlpatterns = patterns(
    'fuel_class.views',
    url(r'fuels/$', 'fuels'),
    url(r'create_fuel/$', 'create_fuel'),
    url(r'remove_fuel/$', 'remove_fuel'),
    url(r'update_fuel/$', 'update_fuel'),
)
