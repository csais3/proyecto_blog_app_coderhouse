from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from blog_app.models import BlogPost, Publisher

# Create your views here.

@login_required
def dummy(request):

    render(request, "blog_app/panel_login.html")

class PanelView(LoginRequiredMixin, ListView):

    queryset = BlogPost.objects.all()
    template_name = "blog_app/blogpost_list.html"
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):

    model = BlogPost
    fields = ['title', 'image', 'text', 'author']
    template_name = "blog_app/blogpost_form.html"
    success_url = reverse_lazy("blog_crud:panel-page")
    permission_required = ("blog_app.add_post")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('blog_crud:panel-page')
    permission_required = ("news_portal.change_article")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog_crud:panel-page')
    context_object_name = 'post'
    permission_required = ("blog_app.delete_article")

class PanelLogin(LoginView):
    template_name = 'blog_app/panel_login.html'
    next_page = reverse_lazy("blog_crud:panel-page")

class PanelLogout(LogoutView):
    template_name = 'blog_app/panel_logout.html'

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'blog_app/crear_cuenta_form.html'
  success_url = reverse_lazy('blog_crud:panel-page')
  form_class = UserCreationForm
  success_message = "Se creo tu perfil satisfactoriamente"

class UserProfile(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Publisher
    template_name = "user_profile/user_detail.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("blog_crud:user-detail", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

