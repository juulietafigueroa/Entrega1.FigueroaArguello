import email
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario


# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada = "678")
    curso.save()
    documento = f"Nombre del curso:{curso.nombre} - Camada:{curso.camada}"
    return HttpResponse(documento)

def cursos(request):
    return render(request, 'appCoder/cursos.html')
   

def profesores(request):
   return render(request, 'appCoder/profesores.html')

def inicio(self): #inicio necesita un loader para que el resto de las plantillas se remonten en esta.
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def estudiantes(self):
    documento = f"Página de estudiantes"
    return HttpResponse(documento)

def entregables(self):
    documento = f"Página de entregables"
    return HttpResponse(documento)

def cursoFormulario(request):
    
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombre = informacion['curso']
        camada = informacion['camada']
        curso = Curso(nombre= nombre, camada= camada )
        curso.save()
        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render (request, 'appCoder/cursoFormulario.html', {'miFormulario': miFormulario})


def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():
           informacion = miFormulario.cleaned_data 
        
           
           profesor = Profesor (nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], profesion =informacion['profesion'])

           profesor.save()

           return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render (request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})


def busquedaCamada(request):
    return render(request, 'appCoder/busquedaCamada.html')

def buscar(request):
    
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada=camada)
        return render(request, 'appCoder/resultadosBusqueda.html', {'cursos':cursos, 'camada':camada})
    else: 
        respuesta="No se ha ingresado ninguna comisión"

    return HttpResponse(respuesta)