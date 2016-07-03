from django.conf.urls import patterns, url


urlpatterns = patterns(
   'hedge_account.views',
    url(r'hedge_accounts/$', 'hedges'),
    url(r'create_hedge_account/$', 'create_hedge_account'),
    url(r'remove_hedge_account/$', 'remove_hedge_account'),

)
