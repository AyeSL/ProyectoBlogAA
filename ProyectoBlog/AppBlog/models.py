from django.db import models

# Create your models here.

#======================= MODELO AUTOR =====================================
class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + ' ' + self.apellido

#======================= MODELO CATEGORÍA  =====================================
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=300)
    
    def __str__(self):
        return self.nombre

#====================== MODELO POST ========================================
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    contenido = models.TextField()
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE,)
    fecha_creacion = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
