from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def renato(request):
    return HttpResponse('<h1>Hello, Renato!</h1>')

def greet(request, name):
    return render(request, 'hello/greet.html',{
        'name': name.capitalize()
    })