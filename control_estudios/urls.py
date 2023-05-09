"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from control_estudios.views import listar_cursos, crear_curso, buscar_cursos,\
    eliminar_curso, editar_curso, EstudianteListView, EstudianteCreateView,\
    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView


urlpatterns = [
    # URLS de cursos
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("eliminar-curso/<int:id>/", eliminar_curso, name="eliminar_curso"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    # URLS de estudiantes
    path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
    path('estudiantes/<int:pk>/', EstudianteDetailView.as_view(), name="ver_estudiante"),
    path('crear-estudiante/', EstudianteCreateView.as_view(), name="crear_estudiante"),
    path('editar-estudiante/<int:pk>/', EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path('eliminar-estudiante/<int:pk>/', EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
]
