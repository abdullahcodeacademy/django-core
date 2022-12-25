from django import template
from ..models import Book

register = template.Library()

@register.inclusion_tag('search_results.html')
def books_for_author(author): 
    books = Book.objects.filter(authors__id=author.id) 
    return {'books': books} 
