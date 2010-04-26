from django.views.generic.list_detail import object_detail

from models import Module

def module_detail(request, year, semester, module_code, *args, **kwargs):
	kwargs['queryset'] = Module.objects.filter(year=year, semester=semester).select_related()
	kwargs['slug'] = module_code
	kwargs['slug_field'] = 'definition__code'
	return object_detail(request, *args, **kwargs)
