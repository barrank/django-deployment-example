# CUSTOM FILTERS

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='cut')
@stringfilter
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, "")

# register.filter('cut', cut)
# #                      ^^^ Function
# #               ^^^^ Name of the filter
