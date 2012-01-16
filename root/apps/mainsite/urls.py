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


if settings.DEBUG:
    # If we are in debug mode, prepend a rule to urlpatterns to serve the static media
    import re
    urlpatterns = patterns('',
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL), 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
        }),
    ) + urlpatterns
