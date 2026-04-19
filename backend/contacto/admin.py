from django.contrib import admin
from .models import MensajeContacto


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'empresa', 'servicio', 'presupuesto', 'leido', 'creado')
    list_editable = ('leido',)
    list_filter = ('leido', 'servicio', 'creado')
    search_fields = ('nombre', 'email', 'empresa', 'mensaje')
    readonly_fields = ('nombre', 'empresa', 'email', 'telefono', 'servicio', 'presupuesto', 'mensaje', 'creado')
    ordering = ('-creado',)
