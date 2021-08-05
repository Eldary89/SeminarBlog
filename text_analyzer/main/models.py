from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    text = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    authors = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True,
        related_name="blog_author"
    )
    upvotes = models.ManyToManyField(
        User, blank=True,
        related_name="blog_upvotes"
    )
    downvotes = models.ManyToManyField(
        User, blank=True,
        related_name="blog_downvotes"
    )

    def __str__(self):
        return f"{self.title} created at {self.created}"
