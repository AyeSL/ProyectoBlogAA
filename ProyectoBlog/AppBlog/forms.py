from django import forms
from .models import Autor, Post, Categoria

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