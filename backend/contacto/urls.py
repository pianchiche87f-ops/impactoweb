from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_contacto, name='enviar_contacto'),
]
