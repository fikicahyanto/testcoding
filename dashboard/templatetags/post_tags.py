from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def linkify_location(message, post_id):
    match = re.search(r'\bdi\s+([A-Za-z\s]+)', message)
    if match:
        location = match.group(1).strip()
        link = f'<a href="/peta/{post_id}/">{location}</a>'
        new_message = message.replace(location, link)
        return mark_safe(new_message)
    return message