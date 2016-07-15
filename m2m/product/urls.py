from django.conf.urls import patterns, url

urlpatterns = patterns(
    'product.views',
    url(r'products/$', 'products'),
    url(r'create_product/$', 'create_product'),
    url(r'remove_product/$', 'remove_product'),
    url(r'update_product/$', 'update_product'),
)
