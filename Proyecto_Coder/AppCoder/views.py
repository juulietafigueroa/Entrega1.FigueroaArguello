from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.

def curso(self):
    curso = Curso(nombre="Desarrollo Web", camada = "678")
    curso.save()
    documento = f"Nombre del curso:{curso.nombre} - Camada:{curso.camada}"
    return HttpResponse(documento)