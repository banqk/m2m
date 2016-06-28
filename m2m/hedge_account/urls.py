from django.conf.urls import patterns, url


urlpatterns = patterns(
   'hedge_account.views',
    url(r'hedges/$', 'hedges'),
    url(r'create_hedge_account/$', 'create_hedge_account'),

)
