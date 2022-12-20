from django.urls import path
from .views import inicio, Home, PostsList, PostDetail, PostCreate, PostUpdate,PostDelete, buscarpost
from .views import AutorList, AutorCreate, AutorUpdate, AutorDelete
from .views import CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDelete
urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', Home.as_view(), name='home'),
    path("posts/post_search", buscarpost , name='buscar'),
    path('posts/posts_list', PostsList.as_view(), name="posts_list"),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts/post_create', PostCreate.as_view(), name='post_create'),
    path('posts/post_update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('posts/post_delete/<int:pk>', PostDelete.as_view(), name='post_delete'),
############ url autores ###########
    path('autor/autor_list', AutorList.as_view(), name='autor_list'),
    path('autor/autor_create', AutorCreate.as_view(), name='autor_create'),
    path('autor/autor_update/<int:pk>', AutorUpdate.as_view(), name='autor_update'),
    path('autor/autor_delete/<int:pk>', AutorDelete.as_view(), name='autor_delete'),

############ url categorias ###########
    path('categoria/categoria_list', CategoriaList.as_view(), name='categoria_list'),
    path('categoria/categoria_create', CategoriaCreate.as_view(), name='categoria_create'),
    path('categoria/categoria_update/<int:pk>', CategoriaUpdate.as_view(), name='categoria_update'),
    path('categoria/categoria_delete/<int:pk>', CategoriaDelete.as_view(), name='categoria_delete'),
]