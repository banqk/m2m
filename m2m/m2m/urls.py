from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'm2m.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('accounts.urls')),
    url(r'^company', include('company.urls')),
    url(r'^api', include('common.urls')),
    url(r'^inventory', include('inventory.urls')),
    url(r'^hedge', include('hedge_account.urls')),
    url(r'^users', include('users.urls')),
    url(r'^counter', include('counter_party.urls')),
    url(r'^product', include('product.urls')),
    url(r'^transaction', include('phy_transaction.urls')),
    url(r'^hedge_tran', include('hedge_transaction.urls')),
    url(r'^fuel', include('fuel_class.urls')),
    url(r'^inst', include('hedge_instrument.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'login.html'}),
]

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
