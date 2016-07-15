from django.conf.urls import patterns, url

urlpatterns = patterns(
    'hedge_transaction.views',
    url(r'hedge_tran/$', 'hedge_tran'),
    url(r'create_hedge_tran/$', 'create_hedge_tran'),
    url(r'remove_hedge_tran/$', 'remove_hedge_tran'),
    url(r'update_hedge_tran/$', 'update_hedge_tran'),
)
