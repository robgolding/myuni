from django.conf.urls.defaults import *

from models import Module

urlpatterns = patterns('',

	url(r'^$', 'django.views.generic.list_detail.object_list',
        {'queryset': Module.objects.all(),
        'template_name': 'modules/module_list.html'},
        name='modules_module_list'),
	
)