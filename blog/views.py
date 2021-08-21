from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Post, Author, Tag


# Create your views here.


def index(request):
    sorted_posts = Post.objects.all().order_by('-date')
    latest_posts = sorted_posts[:3]
    return render(request, 'blog/index.html', {
        'latest_posts': latest_posts,
    })


def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts,
    })


def post_detail(request, slug):
    identify_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identify_post,
    })
