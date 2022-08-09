from django.contrib import admin
from .models import BlogPost, Publisher

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Publisher)