from django.shortcuts import render

from control_estudios.models import Estudiante, Curso


def listar_estudiantes(request):
    contexto = {
        "estudiantes": Estudiante.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_response


def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_response


def crear_curso(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_curso_a_mano.html',
        context=contexto,
    )
    return http_response
