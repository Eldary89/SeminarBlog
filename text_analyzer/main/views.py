from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template import loader
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    template = loader.get_template("index.html")
    return HttpResponse(template.render({"blogs": blogs}, request))


def get_blog_create(request):
    template = loader.get_template("blog_create.html")
    return HttpResponse(template.render({}, request))


def post_blog_create(request):
    if len(request.POST.get("title").strip()) > 0 and len(request.POST.get("text").strip()) > 0:
        Blog.objects.create(
            title=request.POST.get("title").strip(),
            text=request.POST.get("text").strip()
        )
    return redirect(reverse('main:index', kwargs={}))