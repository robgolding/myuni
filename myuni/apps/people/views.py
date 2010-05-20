from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from profiles.views import edit_profile as profiles_edit_profile

@login_required
def edit_profile(request, username, *args, **kwargs):
	if username == request.user.username:
		return profiles_edit_profile(request, *args, **kwargs)
	return HttpResponseRedirect(reverse('people_profile_detail', args=[request.user.username]))
