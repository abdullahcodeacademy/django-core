"""masterdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from masterdjango.views import hello, current_datetime, hours_ahead
from books import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('testview/', views.testview),
    path('time/', current_datetime),
    path('time/plus/<int:offset>/', hours_ahead),
    path('search-form/', views.search_form),
    path('search/', views.search),
    # In urls.py 
    path('hello-su/<str:name>/', views.SuperVillainView.as_view()), 
    path('hello-su/', views.SuperVillainView.as_view()),     
]
