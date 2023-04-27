from django.shortcuts import render


def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel"},
            {"nombre": "Manuela", "apellido": "Gomez"},
            {"nombre": "Ivan", "apellido": "Tomasevich"},
            {"nombre": "Carlos", "apellido": "Perez"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde


def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Python", "comision": "40440"},
            {"nombre": "Frontend", "comision": "1000"},
            {"nombre": "Diseño", "comision": "1001"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_responde
