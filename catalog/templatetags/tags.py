from django import template

register = template.Library()


@register.filter
def modify_path(val):
    if val:
        return f'/media/{val}'
    return f'/media/logo apple.png'

