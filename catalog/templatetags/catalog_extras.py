"""Custom template tags."""
import random

from django import template

from ..models import Mineral

register = template.Library()

@register.simple_tag
def subtraction(num1, num2):
    """Subtract an Return the result"""
    return num1 - num2

@register.filter('random_mineral')
def random_mineral(x):
    """ Return a random id"""
    mineral_ids = Mineral.objects.all().values_list('id', flat=True)
    return random.choice(mineral_ids)


@register.filter('underscore_to_space')
def underscore_to_space(input):
    """Removes underscore and replace with a SPACE"""
    return input.replace('_', ' ')
