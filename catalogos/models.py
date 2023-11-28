from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombreCategoria=models.CharField(max_length=40)
    def __str__(self):
        return self.nombreCategoria     

class Productos(models.Model):    
    idjuego = models.CharField(max_length=20, null=False)
    nombre= models.CharField(max_length=40)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion= models.CharField(max_length = 100)
    existencias= models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    activo = models.BooleanField(default=True, null=True, blank=True)
    creado = models.DateField(auto_now_add=True, blank=True)
    modificado = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nombre     
