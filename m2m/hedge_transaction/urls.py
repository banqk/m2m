from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hedge_transaction.views',
    url(r'hedge_tran/$', 'hedge_tran'),
    url(r'create_ht/$', 'create_hedge_tran'),
    url(r'remove_ht/$', 'remove_ht'),
    url(r'update_ht/$', 'update_ht'),
    url(r'hedge_pos/$', 'hedge_pos'),
    url(r'hedge_price/$', 'hedge_price'),
    url(r'hedge_pos_view/$', 'hedge_pos_view'),
)
