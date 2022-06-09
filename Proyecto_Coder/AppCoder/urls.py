from django.urls import path
from AppCoder.views import profesores,curso,inicio, entregables, cursos, estudiantes, cursoFormulario, profesorFormulario, busquedaCamada, buscar



urlpatterns = [
   path('profesores/', profesores, name='Profesores'),
   path('curso/', curso), 
   path('cursos/', cursos, name='Cursos'),
   path('estudiantes/', estudiantes, name='Estudiantes'),
   path('entregables/', entregables, name='Entregables'),
   path('', inicio, name='Inicio' ), 
   path('cursoformulario/', cursoFormulario, name='cursoFormulario'),
   path('profesorformulario/', profesorFormulario, name='profesorFormulario'),
   path ('busquedaCamada/', busquedaCamada, name='busquedaCamada'),
   path ('buscar/', buscar, name='buscar'),

    
]

