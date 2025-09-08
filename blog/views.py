from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def hello_view(request):
    return HttpResponse("Hello Django")

def home_view(request):
    context = {"name":"Azhar","current_date": datetime.now() }
    return render(request, "blog/home.html",context)