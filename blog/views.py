from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *
# Create your views here.

def hello_view(request):
    return HttpResponse("Hello Django")

def home_view(request):
    posts = Post.objects.all().prefetch_related("comments")
    context = {"name":"Azhar","current_date": datetime.now(),"posts" : posts }
    return render(request, "blog/home.html",context)