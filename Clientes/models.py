from django.db import models

class Clientes(models.Model):
    Masculino = 1
    Femenino = 2
    TYPE_GENER = (
        (Masculino,'Masculino'),
        (Femenino,'Femenino'),
    )
    nombre = models.CharField(max_length=150, verbose_name="Nombres", blank=False)
    apellido = models.CharField(max_length=150, verbose_name="Apellido", blank=False)
    telefono = models.CharField(max_length=50, verbose_name="Telefono", unique=True, blank=False)
    email = models.CharField(max_length=150, verbose_name="Email", blank=False)
    direccion = models.CharField(max_length=150, verbose_name="Direccion", blank=False)
    type_genero = models.PositiveSmallIntegerField(choices=TYPE_GENER)
    mensaje = models.CharField(max_length=150, verbose_name="Mensaje", blank=True)
    def __str__ (self):
        return self.apellido

