"""Custom template tags."""
from django import template
register = template.Library()

@register.simple_tag
def item_count(item):
    """Return the number of items in a list."""
    return len(item)

@register.filter('underscore_to_space')
def underscore_to_space(input):
    """Removes underscore and replace with a SPACE"""
    return input.replace('_', ' ')