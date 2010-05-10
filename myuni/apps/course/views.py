from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail

from models import Module

@login_required
def module_list(request, *args, **kwargs):
	if not kwargs.has_key('queryset'):
		kwargs['queryset'] = request.user.modules_taken.select_related()
	return object_list(request, *args, **kwargs)

def module_detail(request, year, semester, module_code, *args, **kwargs):
	kwargs['queryset'] = Module.objects.filter(year=year, semester=semester).select_related()
	kwargs['slug'] = module_code
	kwargs['slug_field'] = 'definition__code'
	return object_detail(request, *args, **kwargs)
