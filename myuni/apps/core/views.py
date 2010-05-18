from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template
from django.contrib import messages

def index(request, *args, **kwargs):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('dashboard'))
	return direct_to_template(request, *args, **kwargs)

def colophon(request, *args, **kwargs):
	response = direct_to_template(request, *args, **kwargs)
	messages.info(request, 'We hope you enjoyed the colophon!')
	return response
