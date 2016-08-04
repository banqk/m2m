from django.conf.urls import patterns, url
import django.contrib.auth

urlpatterns = patterns(
    'accounts.views',
    url(r'^$', 'index'),
#    url(r'^login/$', 'login'),
#    url(r'^login/$', 'django.contrib.auth.views.login',
#        {'template_name': 'login.html'}),
    url(r'^accounts/$', 'accounts'),
    url(r'^log/$', 'log'),
    url(r'^create_account/$', 'create_account'),
    url(r'^remove_account/$', 'remove_account'),
    url(r'^update_account/$', 'update_account'),
)
