"""Custom template tags."""
import random

from django import template

from ..models import Mineral

register = template.Library()

# @register.simple_tag
# def subtraction(num1, num2):
#     """Subtract an Return the result"""
#     return num1 - num2

@register.simple_tag
def import_report(minerals_json_count, duplicate_count):
    if minerals_json_count == duplicate_count:
        return 'No new records found.'
    else:
        return "Records added successfully (" + str(duplicate_count) + " duplicates ignored)."


@register.filter('random_mineral')
def random_mineral(x):
    """ Return a random id"""
    mineral_ids = Mineral.objects.all().values_list('id', flat=True)
    return random.choice(mineral_ids)


@register.filter('underscore_to_space')
def underscore_to_space(machine_name):
    """Removes underscore and replace with a SPACE"""
    return machine_name.replace('_', ' ')

