from .models import Persona, Asignatura, Asistencia, Alumno, Profesor
from rest_framework import serializers

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ["rut","nombre_real","nombre_usuario","contrasenia","edad","tipo"]

class AsignaturaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields =[ "idCurso","nombre","fecha","rut"]

class AsistenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = [ "idAsistencia","rutProfesor","fecha","hora","rutAlumno","curso"]
        
class AlumnoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ["rut","nombre","apellido","password"]

class ProfesorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ["rut","nombre","apellido","password"]