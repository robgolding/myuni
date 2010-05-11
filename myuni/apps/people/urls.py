from django.conf.urls.defaults import *

from django.contrib.auth.models import User

import views

urlpatterns = patterns('',
	
	url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': User.objects.all().select_related(), 'template_name': 'people/user_list.html'}, name='people_user_list'),
	
	url(r'^(?P<username>.+)/$', 'profiles.views.profile_detail', {'template_name': 'people/user_detail.html'}, name='people_user_detail'),
	
)
