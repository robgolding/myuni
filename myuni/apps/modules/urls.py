from django.conf.urls.defaults import *

from models import Module
import views

urlpatterns = patterns('django.views.generic.list_detail',
	
	url(r'^$', 'object_list', {'queryset': Module.objects.all().select_related(), 'template_name': 'modules/module_list.html'}, name='modules_module_list'),
	
	url(r'^(?P<year>[0-9-]+)/(?P<semester>[\w-]+)/(?P<module_code>\w+)/$', views.module_detail, {'template_name': 'modules/module_detail.html'}, name='modules_module_detail'),
)
