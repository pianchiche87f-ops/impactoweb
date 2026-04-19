from django.db import models


CATEGORIA_CHOICES = [
    ('ecommerce', 'E-commerce'),
    ('corporativo', 'Corporativo'),
    ('landing', 'Landing Page'),
    ('sistema', 'Sistema Web'),
]


class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='portafolio/', blank=True, null=True)
    video_demo_url = models.URLField(blank=True, help_text='URL del video demostrativo (YouTube, Vimeo, etc.)')
    demo_url = models.URLField(blank=True, help_text='Link al sitio demo en vivo')
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cliente = models.CharField(max_length=200, blank=True)
    resultado = models.CharField(max_length=200, blank=True, help_text='Ej: +200% ventas')
    tiempo_entrega = models.CharField(max_length=100, blank=True, help_text='Ej: 2 semanas')
    activo = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0, help_text='Orden de aparición (menor = primero)')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden', '-creado']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.titulo
