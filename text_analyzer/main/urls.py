from django.urls import path
from .views import (
    index, get_blog_create, post_blog_create,
    blog_upvote, blog_downvote, register_view,
    post_register, login_view
)

app_name = 'main'

urlpatterns = [
    path("", index, name="index"),
    path("create_blog/", get_blog_create, name="create_blog"),
    path("post_text/", post_blog_create, name="post_text"),
    path("blog_up/<int:pk>/", blog_upvote, name="blog_up"),
    path("blog_down/<int:pk>/", blog_downvote, name="blog_down"),
    path("register/", register_view, name='register'),
    path("post_register/", post_register, name='post_register'),
    path("login/", login_view, name="login"),
]