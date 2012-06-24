from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mainsite.views import *


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),

    # Test URLs to allow you to see these pages while DEBUG is True
    url(r'^error/404/$', Error404.as_view(), name='404'),
    url(r'^error/500/$', Error500.as_view(), name='500'),
)


if settings.DJANGO_SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )