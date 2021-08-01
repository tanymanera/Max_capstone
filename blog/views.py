from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Put here welcome page')


def posts(request):
    return HttpResponse('Put here all posts')


def post(request, slug):
    return HttpResponse(f'put here post with slug: {slug}')
