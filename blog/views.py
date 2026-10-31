from django.shortcuts import get_object_or_404, render
from .models import Category, Post


def blog(request):
    posts = Post.objects.prefetch_related("categories").select_related("author")
    return render(request, "blog/blog.html", {"posts": posts, "category": None})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.post_set.select_related("author").prefetch_related("categories")
    return render(request, "blog/blog.html", {"posts": posts, "category": category})
