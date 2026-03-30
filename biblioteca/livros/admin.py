from django.contrib import admin
from .models import Autor, Livro

# Register your models here.

admin.site.register(Autor)
admin.site.register(Livro)