from django.contrib import admin
from .models import * # el * es para que importe todos los modelos y no tener que importar uno por uno.

# Register your models here.

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)

