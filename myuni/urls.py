from django.conf.urls.defaults import *
from django.contrib import admin

from myuni.apps.core.views import index

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	url(r'^$', index, {'template': 'index.html'}, name="index"),
	
	url(r'^colophon/$', 'django.views.generic.simple.direct_to_template', {'template': 'colophon.html'}, name="colophon"),
	
	url(r'^dashboard/', include('myuni.apps.dashboard.urls')),
    url(r'^modules/', include('myuni.apps.modules.urls')),

	url(r'^accounts/', include('registration.urls')),
	
)

from django.conf import settings

if settings.SERVE_MEDIA:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)
