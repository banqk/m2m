from django.conf.urls import patterns, url

urlpatterns = patterns(
    'accounts.views',
    url(r'^$', 'index'),
    url(r'^accounts/$', 'accounts'),
    url(r'^log/$', 'log'),
    url(r'^create_account/$', 'create_account'),
)
