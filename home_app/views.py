from django.shortcuts import render
from django.http import HttpResponse

# views go here
def index(request):
  return HttpResponse('<h1>The Greatest Sports Memorabilia Collection</h1>')

# Create your views here.
