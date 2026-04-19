from django.contrib import admin
from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'cliente', 'precio', 'activo', 'orden', 'creado')
    list_editable = ('activo', 'orden')
    list_filter = ('categoria', 'activo')
    search_fields = ('titulo', 'cliente', 'descripcion')
    ordering = ('orden', '-creado')
    fieldsets = (
        ('Información principal', {
            'fields': ('titulo', 'categoria', 'cliente', 'descripcion', 'activo', 'orden')
        }),
        ('Multimedia', {
            'fields': ('imagen', 'video_demo_url', 'demo_url'),
            'description': 'La imagen se muestra en la galería. Al hacer clic se abre el video demo.'
        }),
        ('Resultados y precio', {
            'fields': ('precio', 'resultado', 'tiempo_entrega')
        }),
    )
