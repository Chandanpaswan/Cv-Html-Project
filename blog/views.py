from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def post_list(request):
    query = request.GET.get("q", "").strip()
    posts = BlogPost.objects.filter(is_published=True)
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(excerpt__icontains=query) | Q(tags__icontains=query))
    categories = BlogPost.objects.filter(is_published=True).values_list("category", flat=True).distinct()
    return render(request, "blog/list.html", {"posts": posts, "categories": categories, "query": query})


def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    related = BlogPost.objects.filter(is_published=True, category=post.category).exclude(pk=post.pk)[:3]
    return render(request, "blog/detail.html", {"post": post, "related": related})
