from django.shortcuts import render
from .models import Post

# Create your views here.
from django.shortcuts import render

def blog(request):
    posts = Post.objects.all()  # Obtén todos los posts
    return render(request, "blog/blog.html", {'posts': posts})