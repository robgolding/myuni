from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template

def index(request, template):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('dashboard'))
	return direct_to_template(request, template=template)
