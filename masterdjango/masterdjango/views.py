from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse 
from django.shortcuts import render
import datetime 


def hello(request):
     return HttpResponse("Hello world") 

# def current_datetime(request):
#      now = datetime.datetime.now()
#      html = "<html><body>It is now %s.</body></html>" % now
#      return HttpResponse(html) 

def current_datetime(request):
     now = datetime.datetime.now()
     t = get_template('current_datetime.html')
     values = request.META.items() 
     context = {'current_date': now,'path':values }
     html = t.render(context)
     #html = t.render(Context({'current_date': now}))
     return HttpResponse(html)

def hours_ahead(request, offset):
     try:
         offset = int(offset)
     except ValueError:
         raise Http404()
     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
     #assert False
     html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
     return HttpResponse(html) 



