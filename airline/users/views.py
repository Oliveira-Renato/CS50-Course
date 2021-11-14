from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
def index(request):
  if not request.user.is_authenticated:
    username = request.POST["username"]
    password = request.POST["password"]
    
    return HttpResponseRedirect(reverse("login"))

def login_view(request):
  return render(request, "users/login.html")

def logout_view(request):
  pass
