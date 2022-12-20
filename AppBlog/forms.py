from django import forms
from .models import Autor, Post, Categoria

class AutorForm(forms.ModelForm):
    #Metaclase Meta
    class Meta:
        model = Autor
        fields = [
                'id', 
                'nombre',
                'apellido',
                'fecha_nacimiento',
                'nacionalidad',
                ]
        
        labels = {
            'nombre': "Nombre",
            'apellido': "Apellido",
            'fecha_nacimiento': "Fecha de nacimiento",
            'nacionalidad': "Nacionalidad",
        }
        #Los widgets son los tipos de nuestras inputs
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad'}),
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Fecha yyyy-mm-dd', }),
            
        }

class PostForm(forms.ModelForm):
    #Metaclase Meta
    class Meta:
        model = Post
        fields = [
                'id', 
                'titulo',
                'subtitulo',
                'descripcion',
                'contenido',
                'autor', 
                'fecha_creacion',
                'categoria',
                ]
        
        labels = {
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'descripcion': 'Descripción',
            'contenido': 'Contenido',
            'autor': 'Autor',
            'fecha_creacion': 'Fecha Creación',
            'categoria': 'Categoría',
        }
        #Los widgets son los tipos de nuestras inputs
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtítulo'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 22, 'style': 'resize:none;'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'fecha_creacion': forms.DateInput(format=('%Y-%m-%d'), attrs={'placeholder': 'Fecha yyyy-mm-dd', }),
        }
        
class CategoriaForm(forms.ModelForm):
    #Metaclase Meta
    class Meta:
        model = Categoria
        fields = [
                'id', 
                'nombre',
                'descripcion',
                ]
        
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
        }
        #Los widgets son los tipos de nuestras inputs
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripcion'}),
        }