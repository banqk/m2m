from django.conf.urls import patterns, url

urlpatterns = patterns(
    'users.views',
    url(r'users/$', 'users'),
    url(r'create_user/$', 'create_user'),
    url(r'update/$', 'update'),
)
