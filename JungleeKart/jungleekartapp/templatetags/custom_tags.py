from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.simple_tag
def ratings(rating):
    full_star = '&#9733; '  # ★
    empty_star = '&#9734; '  # ☆
    full_stars = full_star * rating
    empty_stars = empty_star * (5 - rating)
    return mark_safe(full_stars + empty_stars)