from django.db import models

class Curso(models.Model):

    nombre=models.CharField(max_length=40) #indicar campo en este caso es de palabras y ponemos que puede tener un max de 40
    camada=models.IntegerField() #indicamos que es un campo de numero

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() #EmailField se usa para pedir un email

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
       nombre = models.CharField(max_length=30) 
       fecha_de_entrega = models.DateField()
       entregado = models.BooleanField()


