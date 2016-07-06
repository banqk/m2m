from django.conf.urls import include, url
from django.contrib import admin

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
]
