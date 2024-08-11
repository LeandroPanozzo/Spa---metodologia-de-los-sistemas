#Las rutas determinan qué vista se debe ejecutar para cada URL.
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    #Esta ruta vincula la URL raíz ('') con la vista home. El nombre Inicio-Spa es un identificador que puede 
    # usarse en las plantillas para generar enlaces de manera dinámica.
    path('', PostListView.as_view(), name='Inicio-Spa'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='About-Spa'),
]