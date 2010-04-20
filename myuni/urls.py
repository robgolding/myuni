from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'myuni/index.html'}, name="index"),
	url(r'^dashboard/$', 'django.views.generic.simple.direct_to_template', {'template': 'myuni/dashboard.html'}, name="myuni_dashboard"),
	url(r'^colophon/$', 'django.views.generic.simple.direct_to_template', {'template': 'myuni/colophon.html'}, name="myuni_colophon"),
	
	url(r'^accounts/', include('registration.urls')),
	
)

from django.conf import settings

if settings.SERVE_MEDIA:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)
