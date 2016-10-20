from django.conf.urls import patterns, url

urlpatterns = patterns(
    'common.views',
    url(r'account', 'account'),
    url(r'user', 'user'),
    url(r'company', 'company'),
    url(r'inventory', 'inventory'),
    url(r'hedge/$', 'hedge'),
    url(r'hedge_tran/$', 'hedge_tran'),
    url(r'product', 'product'),
    url(r'counter', 'counter'),
    url(r'fuel', 'fuel_class'),
    url(r'get_prod', 'get_prod'),
)
