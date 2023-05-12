from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    http_response = HttpResponse(saludo)
    return http_response


def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    http_response = HttpResponse(saludo)
    return http_response


def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    http_response = HttpResponse(texto)
    return http_response


def saludar_con_html(request):
    contexto = {
        "usuario": "EJEMPLO"
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    )
    return http_responde


def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_estudios/index.html',
        context=contexto,
    )
    return http_response
