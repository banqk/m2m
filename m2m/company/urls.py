from django.conf.urls import patterns, url

urlpatterns = patterns(
    'company.views',
    url(r'companies/$', 'companies'),
    url(r'create_company/$', 'create_company'),
    url(r'remove_company/$', 'remove_company'),
)
