from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from mainsite.views import *

admin.autodiscover()

handler500 = 'mainsite.views.error500'
handler404 = 'mainsite.views.error404'

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', TestView.as_view(), name='test'),

    (r'', include('SAMPLEAPP.urls')),
)


if not settings.DEBUG or settings.DJANGO_SERVE_STATIC:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )