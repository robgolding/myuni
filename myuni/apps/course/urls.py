from django.conf.urls.defaults import *

from models import Module
import views

module_urls = patterns('',
	
	url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': Module.objects.all().select_related(), 'template_name': 'course/modules/module_list.html'}, name='course_module_list'),
	
	url(r'^(?P<year>[0-9-]+)/(?P<semester>[\w-]+)/(?P<module_code>\w+)/$', views.module_detail, {'template_name': 'course/modules/module_detail.html'}, name='course_module_detail'),
	
)

urlpatterns = patterns('',
	url(r'^modules/', include(module_urls)),
)
