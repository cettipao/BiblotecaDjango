from django.db import models

# Create your models here.



class Ejemplar(models.Model):
    libro = models.ForeignKey(
        'Libro',
        on_delete=models.CASCADE,
        null=False
    )
    localizacion = models.CharField(max_length = 30,null=False)
    def __str__(self):
        return str("{} de {}".format(self.localizacion,self.libro.titulo))

class Libro(models.Model):
    titulo = models.CharField(max_length = 30,null=False)
    editorial = models.CharField(max_length = 30,null=False)
    paginas = models.IntegerField(null=False)
    autor = models.ForeignKey(
        'Autor',
        on_delete=models.CASCADE,
        null=False
    )
    def __str__(self):
        return str(self.titulo)

class Autor(models.Model):
    nombre = models.CharField(max_length = 30,null=False)
    def __str__(self):
        return str(self.nombre)