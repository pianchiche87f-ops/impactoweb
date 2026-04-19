from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Proyecto


@require_GET
def lista_proyectos(request):
    """Devuelve proyectos activos. Filtra por ?categoria=ecommerce"""
    qs = Proyecto.objects.filter(activo=True)
    categoria = request.GET.get('categoria')
    if categoria and categoria != 'all':
        qs = qs.filter(categoria=categoria)

    data = []
    for p in qs:
        imagen_url = None
        if p.imagen:
            imagen_url = request.build_absolute_uri(p.imagen.url)
        data.append({
            'id': p.id,
            'titulo': p.titulo,
            'categoria': p.categoria,
            'descripcion': p.descripcion,
            'imagen_url': imagen_url,
            'video_demo_url': p.video_demo_url,
            'demo_url': p.demo_url,
            'precio': str(p.precio) if p.precio else None,
            'cliente': p.cliente,
            'resultado': p.resultado,
            'tiempo_entrega': p.tiempo_entrega,
        })
    return JsonResponse({'proyectos': data})
