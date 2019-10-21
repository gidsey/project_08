"""Custom template tags."""
from django import template

register = template.Library()


@register.simple_tag
def import_report(minerals_json_count, duplicate_count):
    if minerals_json_count == duplicate_count:
        return 'No new records found.'
    else:
        num_added = minerals_json_count - duplicate_count
        if num_added > 1:
            rec = ' records'
        else:
            rec = ' record'
        return str(num_added) + rec +\
            " added successfully (" + str(duplicate_count) +\
            " duplicates ignored)."


@register.filter('underscore_to_space')
def underscore_to_space(machine_name):
    """Removes underscore and replace with a SPACE"""
    return machine_name.replace('_', ' ')
