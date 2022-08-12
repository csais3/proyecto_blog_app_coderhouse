from django.shortcuts import render
from django.views.generic import (ListView, DetailView, 
        TemplateView)
from blog_app.models import BlogPost
# Create your views here.

class PostListView(ListView):
    # Vistal para ver el listado de posts creados.
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    template_name = "blog_app/blogpost.html"

class PostDetailView(DetailView):
    # Vista para ver un post individual dependiendo la PrimaryKey del post
    model = BlogPost
    context_object_name = "post"


class About(TemplateView):
    # Vista para ver un template estatico en este caso el del link Nosotros
    template_name = "blog_app/about.html"

class MainPageView(TemplateView):
    # Vista de index como template estatico.
    template_name = "blog_app/index.html"

