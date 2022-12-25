from django import template
from ..models import Book

register = template.Library()

@register.simple_tag
def books_for_author(author): 
    books = Book.objects.filter(authors__id=author.id) 
    return books

@register.filter(name='test') 
def test(value,arg): 
    """Removes all values of arg from the given string""" 
    return value.upper()+' '+arg

