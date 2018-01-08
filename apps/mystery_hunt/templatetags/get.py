from django import template

register = template.Library()

@register.filter
def get(obj, attr):
	"""Combination get from dictionary and get object attribute """
	try:
		return obj.get(attr)
	except AttributeError:
		return getattr(obj, attr)
