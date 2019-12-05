from django import template
from django.utils.safestring import mark_safe
import markdown2

from presents.models import Person

register = template.Library()


@register.simple_tag
def newest_present():
    ''' gets most recent present added to the person's library'''
    return Person.objects.latest('created_at')


@register.inclusion_tag('presents/person_nav.html')
def nav_persons_list():
    '''returns dict of persons to display as nav model'''
    persons = Person.objects.all()
    return {'persons': persons}


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)
