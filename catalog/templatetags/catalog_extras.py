"""Custom template tags."""
from django import template
register = template.Library()

@register.simple_tag
def item_count(item):
    """Return the number of items in a list."""
    return len(item)

# @register.filter
# def to_class_name(value):
#     return value._meta.get_fields()

@register.filter('prepend_ins_name')
def prepend_ins_name(field):
    """prepend 'mineral.' to the field name"""
    output = 'mineral.' + field
    return output
