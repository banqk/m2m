from django.conf.urls import patterns, url


urlpatterns = patterns(
   'inventory.views',
    url(r'inventories/$', 'inventories'),
    url(r'create_inventory/$', 'create_inventory'),
    url(r'remove_inventory/$', 'remove_inventory'),
    url(r'update_inventory/$', 'update_inventory'),
    url(r'add_product/$', 'add_product'),
    url(r'invent_summ/$', 'invent_summ'),
    url(r'invent_summ_hedge/$', 'invent_summ_hedge'),

)
