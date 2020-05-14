from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length = 30,null=False)
    editorial = models.CharField(max_length = 30,null=False)
    paginas = models.IntegerField(null=False)

class Autor(models.Model):
    nombre = models.CharField(max_length = 30,null=False)
    def __str__(self):
        return str(self.nombre)