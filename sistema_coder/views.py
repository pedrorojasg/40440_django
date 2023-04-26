from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html


def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    pagina_html = HttpResponse(texto)
    return pagina_html


def saludar_con_html(request):
    contexto = {
        "usuario": "Pedro"
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    )
    return http_responde
