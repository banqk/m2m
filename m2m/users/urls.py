from django.conf.urls import patterns, url

urlpatterns = patterns(
    'users.views',
    url(r'users/$', 'users'),
)
