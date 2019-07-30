"""Custom template tags."""
from django import template
register = template.Library()

@register.simple_tag
def item_count(item):
    """Return the number of items in a list."""
    return len(item)

@register.filter
def to_class_name(value):
    return value._meta.get_fields()

