from django.conf.urls import patterns, url

urlpatterns = patterns(
    'phy_transaction.views',
    url(r'physical/$', 'physicals'),
    url(r'create_phy/$', 'create_physical'),
    url(r'remove_physical/$', 'remove_physical'),
    url(r'update_physical/$', 'update_physical'),
)
