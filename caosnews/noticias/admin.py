from django.contrib import admin
from .models import Categoria, Noticia
# Register your models here.

class NoticasAdmin(admin.ModelAdmin):
    list_display = ['nombre','categoria','anio']
    search_fields = ['nombre','categoria']
    list_filter =['anio']
    list_per_page = 20

admin.site.register(Categoria)
admin.site.register(Noticia)