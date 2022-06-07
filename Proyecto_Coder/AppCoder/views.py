from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada = "678")
    curso.save()
    documento = f"Nombre del curso:{curso.nombre} - Camada:{curso.camada}"
    return HttpResponse(documento)

def profesores(self):
    documento = f"Página de profesores"
    return HttpResponse(documento)

def plantilla1(self):
    plantilla = loader.get_template('plantilla.html')
    documento = plantilla.render()
    return HttpResponse(documento)