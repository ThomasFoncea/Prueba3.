from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    anio = models.IntegerField()
    def __str__(self):
        return self.nombre
    
    