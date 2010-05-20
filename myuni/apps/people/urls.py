from django.conf.urls.defaults import *

from django.contrib.auth.models import User

import views

urlpatterns = patterns('',
	
	url(r'^$', 'django.views.generic.list_detail.object_list', {'queryset': User.objects.all().select_related(), 'template_name': 'people/profile_list.html'}, name='people_profile_list'),
	
	
	# specify the profile_detail view twice, so the profile app doesn't try and redirect to a non-existent named URL
	url(r'^(?P<username>\w+)/$', 'profiles.views.profile_detail', {'template_name': 'people/profile_detail.html'}, name='people_profile_detail'),
	url(r'^(?P<username>\w+)/$', 'profiles.views.profile_detail', {'template_name': 'people/profile_detail.html'}, name='profiles_profile_detail'),
	
	url(r'^(?P<username>\w+)/edit/$', 'myuni.apps.people.views.edit_profile', {'template_name': 'people/edit_profile.html'}, name='people_edit_profile'),
	
)
