from django.conf.urls import patterns, url


urlpatterns = patterns(
   'inventory.views',
    url(r'inventories/$', 'inventories'),
    url(r'create_inventory/$', 'create_inventory'),
    url(r'remove_inventory/$', 'remove_inventory'),

)
