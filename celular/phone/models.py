from django.db import models

# Create your models here.

#TABLA DE USUARIOS

class Usuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=8)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=15, blank=True)

    def _str_(self):
         return self.username

#TABLA DE PRODUCTOS

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='productos')

    def _str_(self):
        return self.nombre

