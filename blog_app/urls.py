from django.urls import path
from .views import MainPageView, PostDetailView, About, PostListView

app_name = "blog_app" # nombre de la aplicacion
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', About.as_view(), name='about'),
    path('posts/', PostListView.as_view() , name = 'blogpost' ),

    
]
