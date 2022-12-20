from django.contrib import admin
from .models import Categoria, Post, Autor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Autor)

# python manage.py createsuperuser
# Superusuario: admin - password: 1234567