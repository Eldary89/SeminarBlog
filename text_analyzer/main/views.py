from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from .models import Blog
from .forms import RegisterForm


def index(request):
    blogs = Blog.objects.all().order_by('-votes')
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


def blog_upvote(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.votes += 1
    blog.save()
    return redirect(reverse('main:index', kwargs={}))


def blog_downvote(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.votes -= 1
    blog.save()
    return redirect(reverse('main:index', kwargs={}))


def register_view(request):
    template = loader.get_template("register.html")
    return HttpResponse(template.render({}, request))


def login_view(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({}, request))


def post_register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        return redirect(reverse("main:index", kwargs={}))
    template = loader.get_template("register.html")
    return HttpResponse(template.render({"error": form.errors}, request))
