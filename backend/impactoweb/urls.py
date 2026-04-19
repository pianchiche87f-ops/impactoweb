from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from . import views


def health_check(request):
    return JsonResponse({'status': 'ok'})


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Health check
    path('health/', health_check),

    # API endpoints
    path('api/portafolio/', include('portafolio.urls')),
    path('api/contacto/', include('contacto.urls')),

    # Páginas del frontend
    path('', views.index, name='home'),
    path('servicios/', views.servicios, name='servicios'),
    path('precios/', views.precios, name='precios'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
]

# Servir media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
