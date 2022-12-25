from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from django.views.generic import View

# Create your views here.
def search_form(request): 
    return render(request, 'search_form.html') 

def search(request): 
    errors = [] 
    if 'q' in request.GET: 
        q = request.GET['q'] 
        if not q: 
            errors.append('Enter a search term.') 
        elif len(q) > 20: 
            errors.append('Please enter at most 20 characters.') 
        else: 
            books = Book.objects.filter(title__icontains=q) 
            return render(request, 'books/search_results.html', 
                          {'books': books, 'query': q}) 
    return render(request, 'search_form.html', 
                  {'errors': errors}) 

class GreetView(View): 
    greeting = "Hello {}!" 
    default_name = "World" 
    def get(self, request, **kwargs): 
        name = kwargs.pop("name", self.default_name) 
        return HttpResponse(self.greeting.format(name)) 
 
class SuperVillainView(GreetView): 
    greeting = "We are the future, {}. Not them. " 
    default_name = "my friend" 

def testview(request):
    return render(request, 'books/test.html', context={})
