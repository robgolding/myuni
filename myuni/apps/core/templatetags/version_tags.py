"""
Creates a template tag called {% version %} that returns the current version
(as specified in myuni.VERSION, and formatted by myuni.get_version().

Spaces are replaced with hyphens in the version, e.g.:
	
	0.1 dev 1 hg-10:3c87 -> 0.1-dev-1-hg-10:3c87

"""

from django import template
import myuni

register = template.Library()

@register.simple_tag
def version():
    """
    Output the version:

    	{% version %}
    
    """
    return myuni.get_version().replace(' ', '-')
