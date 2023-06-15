from urllib.parse import urlparse

from django import template

register = template.Library()


@register.filter
def basename(value):
    return urlparse(value).path.split('/')[-1]