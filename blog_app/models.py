from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    # Model to make a post.

    title = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField(upload_to="post", null=True, blank=True)
    author = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title