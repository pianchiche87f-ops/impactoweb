from django.db import models


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    servicio = models.CharField(max_length=100, blank=True)
    presupuesto = models.CharField(max_length=100, blank=True)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado']
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'

    def __str__(self):
        return f'{self.nombre} — {self.email} ({self.creado.strftime("%d/%m/%Y")})'
