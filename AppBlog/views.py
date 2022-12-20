from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Categoria, Autor
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from .forms import PostForm, AutorForm , CategoriaForm

# Create your views here.
def inicio(request):
    return render(request, 'componentes/inicio.html');

def buscarpost(request):
    return render(request, "home.html")

def buscar(request):
    if request.GET["id"]:
        id = request.GET['id']
        posts = Post.objects.filter(id=id)
        return render(request,"post/post_search.html",{"posts": posts, "id": id})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

class Home(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha_creacion')
    template_name ='home.html'


##################  Clases de Posts ##############################

class PostsList(ListView):
    model = Post
    queryset = Post.objects.order_by('-fecha_creacion')
    template_name='post/posts_list.html'

class PostDetail(DetailView):
    model =  Post
    template_name = 'post/post_detail.html'

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('posts_list')

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('posts_list')

class PostDelete(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('posts_list')

##################  Clases de Autores ##############################

class AutorList(ListView):
    model = Autor
    queryset = Autor.objects.order_by('nombre')
    template_name= 'autor/autor_list.html'

class AutorCreate(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/autor_create.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdate(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor/autor_create.html'
    success_url = reverse_lazy('autor_list')

class AutorDelete(DeleteView):
    model = Autor
    template_name = 'autor/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

##################  Clases de Categorías ##############################

class CategoriaList(ListView):
    model = Categoria
    queryset = Categoria.objects.order_by('nombre')
    template_name= 'categoria/categoria_list.html'

class CategoriaCreate(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_create.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdate(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_create.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')