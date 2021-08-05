from django.db import models


class Blog(models.Model):
    text = models.CharField(max_length=1000)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} created at {self.created}"
