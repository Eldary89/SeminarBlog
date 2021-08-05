from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .models import Blog
from .forms import RegisterForm


def index(request):
    blogs = [{
        "id": blog.id,
        "text": blog.text,
        "title": blog.title,
        "author": blog.authors.username if blog.authors else "Unknown",
        "created": blog.created,
        "votes": blog.upvotes.count() - blog.downvotes.count(),
        "is_voted": blog.upvotes.filter(username=request.user.username).exists() \
                    or blog.downvotes.filter(username=request.user.username).exists()
    } for blog in Blog.objects.all()]
    template = loader.get_template("index.html")
    return HttpResponse(template.render({"blogs": blogs}, request))


@login_required
def get_blog_create(request):
    template = loader.get_template("blog_create.html")
    return HttpResponse(template.render({}, request))


@login_required
def post_blog_create(request):
    if len(request.POST.get("title").strip()) > 0 and len(request.POST.get("text").strip()) > 0:
        Blog.objects.create(
            title=request.POST.get("title").strip(),
            text=request.POST.get("text").strip(),
            authors=request.user
        )
    return redirect(reverse('main:index', kwargs={}))


@login_required
def blog_upvote(request, pk):
    blog = Blog.objects.get(pk=pk)
    if not blog.upvotes.filter(username=request.user.username).exists() and \
            not blog.downvotes.filter(username=request.user.username).exists():
        blog.upvotes.add(request.user)
    return redirect(reverse('main:index', kwargs={}))


@login_required
def blog_downvote(request, pk):
    blog = Blog.objects.get(pk=pk)
    if not blog.downvotes.filter(username=request.user.username).exists() and \
            not blog.upvotes.filter(username=request.user.username).exists():
        blog.downvotes.add(request.user)
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
        return redirect(reverse("main:login", kwargs={}))
    template = loader.get_template("register.html")
    return HttpResponse(template.render({"error": form.errors}, request))


def post_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect(reverse('main:index', kwargs={}))
    return redirect(reverse('main:login', kwargs={}))


def logout_view(request):
    logout(request)
    return redirect(reverse("main:index", kwargs={}))
