from django import template

register = template.Library()

@register.filter
def select_quiz(queryset, i):
    return queryset[i]
