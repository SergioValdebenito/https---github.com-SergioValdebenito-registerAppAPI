from django.contrib import admin
from .models import Asignatura, Asistencia, Alumno, Profesor, Persona

# Register your models here.
admin.site.register(Asistencia)
admin.site.register(Asignatura)
admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Persona)