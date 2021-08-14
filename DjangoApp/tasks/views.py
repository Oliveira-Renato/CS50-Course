from django.shortcuts import render

tasks = ['daa','dii','duu']

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html', {
        'tasks':tasks
    })