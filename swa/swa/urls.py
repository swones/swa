from django.conf.urls import include, url
from django.contrib import admin

from web import urls


urlpatterns = [
    url(r'^web/', include(urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
