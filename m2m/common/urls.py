from django.conf.urls import patterns, url

urlpatterns = patterns(
    'common.views',
    url(r'account', 'account'),
    url(r'company', 'company'),
)
