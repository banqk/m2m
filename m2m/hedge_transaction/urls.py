from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hedge_transaction.views',
    url(r'hedge_tran/$', 'hedge_tran'),
    url(r'create_ht/$', 'create_hedge_tran'),
    url(r'remove_ht/$', 'remove_ht'),
    url(r'update_ht/$', 'update_ht'),
)
