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
    # Vista para ver el Crud del planel. Es necesario hacer loggin para poder entrar

    queryset = BlogPost.objects.all()
    template_name = "blog_app/blogpost_list.html"
    context_object_name = 'posts'

class PostCreateView(LoginRequiredMixin, CreateView):
    # Vista para crear post. Es necesario estar registrado y hacer login para poder crear.
    model = BlogPost
    fields = ['title', 'image', 'text', 'author']
    template_name = "blog_app/blogpost_form.html"
    success_url = reverse_lazy("blog_crud:panel-page")
    permission_required = ("blog_app.add_post")

class PostUpdateView(LoginRequiredMixin, UpdateView):
    # Vista para actualizar el post. Es necesario hacer loggin para poder actualizarlo.
    model = BlogPost
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('blog_crud:panel-page')
    permission_required = ("news_portal.change_article")

class PostDeleteView(LoginRequiredMixin, DeleteView):
    # Vista para eliminar post. Es necesario estar registrado y hacer loggin para poder eliminar.
    model = BlogPost
    success_url = reverse_lazy('blog_crud:panel-page')
    context_object_name = 'post'
    permission_required = ("blog_app.delete_article")

class PanelLogin(LoginView):
    # Vista para hacer login del Crud
    template_name = 'blog_app/panel_login.html'
    next_page = reverse_lazy("blog_crud:panel-page")

class PanelLogout(LogoutView):
    # Vista para hacer logout.
    template_name = 'blog_app/panel_logout.html'

class SignUpView(SuccessMessageMixin, CreateView):
    # Vista par registrarse en la pagina web.
    template_name = 'blog_app/crear_cuenta_form.html'
    success_url = reverse_lazy('blog_crud:panel-page')
    form_class = UserCreationForm
    success_message = "Se creo tu perfil satisfactoriamente"

class UserProfile(LoginRequiredMixin,UserPassesTestMixin, DetailView):
    # Vista para poder actualizar el perfil de el usuario que esta logged in.
    model = Publisher
    template_name = "user_profile/user_detail.html"

    # Funcion para que solo puedas ver los detalles del pefil del usuario del que estas loggeado
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    # Vista para actualizar el perfil del usuario en el cual estas loggeado.
    model = User
    template_name = "user_profile/user_form.html"
    fields = ["username", "email", "first_name", "last_name"]

    # Funcion para regresar a la pagina de perfil despues de actualizar.
    def get_success_url(self):
        return reverse_lazy("blog_crud:user-detail", kwargs={"pk": self.request.user.id})

    # Funcion para comprobar que solo puedas actualizar el perfil del usuario en el que estas loggeado.
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

