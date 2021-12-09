from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField

# Create your models here.


class Persona(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre_real = models.CharField(max_length=45)
    nombre_usuario = models.CharField(max_length=45)
    contrasenia = models.CharField(max_length=30)
    edad = models.IntegerField(default=18)
    tipo = models.IntegerField()

    def __str__(self):
        return self.rut





class Profesor(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.rut+' '+self.nombre


class Alumno(models.Model):
    rut = models.CharField(primary_key=True,max_length=12)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.rut+' '+self.nombre



class Asignatura(models.Model):
    idCurso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45)
    fecha = models.DateField()
    rut = models.ForeignKey(Profesor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idCurso)+' '+self.nombre+' '+self.rut.nombre


class Asistencia(models.Model):
    idAsistencia = models.IntegerField(primary_key=True)
    rutProfesor = models.ForeignKey(Profesor,on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    curso = models.ForeignKey(Asignatura,on_delete=models.CASCADE,default=1)
    rutAlumno = models.ForeignKey(Alumno,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idAsistencia)