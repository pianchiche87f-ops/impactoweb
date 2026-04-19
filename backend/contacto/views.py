import json
import re
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import MensajeContacto

EMAIL_RE = re.compile(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$')


@csrf_exempt
@require_POST
def enviar_contacto(request):
    """Recibe el formulario, valida, guarda en BD y envía email."""
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        data = request.POST.dict()

    nombre  = data.get('nombre', '').strip()[:200]
    email   = data.get('email', '').strip()[:254]
    mensaje = data.get('mensaje', '').strip()[:5000]

    # Validación
    if not nombre or not email or not mensaje:
        return JsonResponse({'ok': False, 'error': 'Nombre, email y mensaje son obligatorios.'}, status=400)
    if not EMAIL_RE.match(email):
        return JsonResponse({'ok': False, 'error': 'El correo electrónico no es válido.'}, status=400)

    # Guardar en base de datos
    msg = MensajeContacto.objects.create(
        nombre=nombre,
        empresa=data.get('empresa', '').strip()[:200],
        email=email,
        telefono=data.get('telefono', '').strip()[:30],
        servicio=data.get('servicio', '').strip()[:100],
        presupuesto=data.get('presupuesto', '').strip()[:100],
        mensaje=mensaje,
    )

    # Email al administrador
    asunto = f'[ImpactoWeb] Nuevo mensaje de {nombre}'
    cuerpo = (
        f"Nuevo mensaje de contacto recibido en ImpactoWeb:\n\n"
        f"Nombre:      {nombre}\n"
        f"Empresa:     {data.get('empresa', '—')}\n"
        f"Email:       {email}\n"
        f"Teléfono:    {data.get('telefono', '—')}\n"
        f"Servicio:    {data.get('servicio', '—')}\n"
        f"Presupuesto: {data.get('presupuesto', '—')}\n\n"
        f"Mensaje:\n{mensaje}\n\n"
        f"---\nRecibido el {msg.creado.strftime('%d/%m/%Y a las %H:%M')}"
    )

    try:
        send_mail(
            subject=asunto,
            message=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        # Confirmación al cliente
        send_mail(
            subject='Recibimos tu mensaje — ImpactoWeb',
            message=(
                f'Hola {nombre},\n\n'
                'Gracias por contactarnos. Revisaremos tu mensaje y te '
                'responderemos en menos de 1 hora en horario laboral.\n\n'
                'Equipo ImpactoWeb'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=True,
        )
    except Exception:
        # Mensaje guardado en BD aunque falle el email
        pass

    return JsonResponse({'ok': True, 'mensaje': 'Mensaje enviado correctamente.'})
