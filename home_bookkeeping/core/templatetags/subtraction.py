from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    if not value or not arg:
        return 'Нет разницы'
    return value - arg
