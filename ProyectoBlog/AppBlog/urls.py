from django.urls import path
from .views import inicio, Home, PostsList, PostDetail, PostCreate, PostUpdate,PostDelete, buscarpost

urlpatterns = [
    path('', inicio, name='inicio'),
    path('home/', Home.as_view(), name='home'),
    path("posts/post_search", buscarpost , name='buscar'),
    path('posts/posts_list', PostsList.as_view(), name="posts_list"),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('posts/post_create', PostCreate.as_view(), name='post_create'),
    path('posts/post_update/<int:pk>', PostUpdate.as_view(), name='post_update'),
    path('posts/post_deletee/<int:pk>', PostDelete.as_view(), name='post_delete'),


]
