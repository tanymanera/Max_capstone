from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def posts(request):
    return HttpResponse('Put here all posts')


def post_details(request, slug):
    return HttpResponse(f'put here post with slug: {slug}')
