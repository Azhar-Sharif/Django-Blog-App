from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import Post
from .forms import PostForm

def hello_view(request):
    return HttpResponse("Hello Django")

def home_view(request):
    posts = Post.objects.all().prefetch_related('comments')
    context = {
        'name': 'User',
        'current_date': datetime.now(),
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_delete.html', {'post': post})