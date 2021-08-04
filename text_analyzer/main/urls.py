from django.urls import path
from .views import index, get_blog_create, post_blog_create

app_name = 'main'

urlpatterns = [
    path("", index, name="index"),
    path("create_blog/", get_blog_create, name="create_blog"),
    path("post_text/", post_blog_create, name="post_text")
]