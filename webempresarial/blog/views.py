from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()  # Obtén todos los posts
    return render(request, "blog/blog.html", {'posts': posts})

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Obtén la categoría o lanza 404
    return render(request, "blog/category.html", {'category': category})