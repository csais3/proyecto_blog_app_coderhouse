from django.urls import path
from .views import (PanelView, PostCreateView, PostDeleteView, PostUpdateView, 
                    PanelLogin, PanelLogout, SignUpView, dummy, UserProfile, UserUpdate)

app_name = "blog_crud"
urlpatterns = [
    path('panel-page/', PanelView.as_view(), name="panel-page"),
    path('post/crear', PostCreateView.as_view(), name='post-create'),
    path('post/<pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<pk>/eliminar', PostDeleteView.as_view(), name='post-delete'),
    path("login/", PanelLogin.as_view(), name="panel-login"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
    path("signup/", SignUpView.as_view(), name="panel-signup"),
    path('dummy', dummy, name="dummy"),
    path("user/<pk>", UserProfile.as_view(), name="user-detail"),
    path("user/<pk>/edit", UserUpdate.as_view(), name="user-update"),

    
]