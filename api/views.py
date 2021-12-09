from django.shortcuts import render
from .models import Persona, Asistencia, Asignatura, Profesor, Alumno
from .serializers import PersonaSerializers, AsistenciaSerializers, AsignaturaSerializers, ProfesorSerializers, AlumnoSerializers
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


class PersonaViewSet(generics.CreateAPIView):
    queryset= Persona.objects.all()
    serializer_class = PersonaSerializers

class PersonaBuscarViewSet(generics.ListAPIView):
    serializer_class = PersonaSerializers
    queryset= Persona.objects.all()

    '''
    def get_queryset(self):
        elrut= self.kwargs["rut"]
        return Persona.objects.filter(rut=elrut)

    '''
    



class AsistenciaListarViewSet(generics.ListAPIView):
    queryset = Asistencia.objects.all()
    serializer_class= AsistenciaSerializers


class AsignaturaViewSet(generics.CreateAPIView):
    queryset= Asignatura.objects.all()
    serializer_class= AsignaturaSerializers


class ProfesorViewSet(generics.ListAPIView):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializers

class ProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = ProfesorSerializers
    def get_queryset(self):
        elrut= self.kwargs["rut"]
        return Profesor.objects.filter(rut=elrut)

class CursoProfesorBuscarViewSet(generics.ListAPIView):
    serializer_class = AsignaturaSerializers
    def get_queryset(self):
        elrut= self.kwargs["rutp"]
        return Asignatura.objects.filter(rut=elrut)

class AsistenciaViewSet(generics.CreateAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializers

class AsistenciaListarViewSet(generics.ListAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializers

@csrf_exempt
def ProfesorApi(request,id=0):
    if request.method=='POST':
        print("identificador:"+str(id))
        if id==0:
            profesores = Profesor.objects.all()
            profesor_serializar = ProfesorSerializers(profesores,many=True)
        else:
            profesores = Profesor.objects.filter(rut=id)
            profesor_serializar = ProfesorSerializers(profesores,many=True)
        return JsonResponse(profesor_serializar.data,safe=False)
    return JsonResponse("sin metodo",safe=False)

@csrf_exempt
def AlumnoApi(request,id=0):
    if request.method=='POST':
        print("identificador:"+str(id))
        if id==0:
            alumnos = Alumno.objects.all()
            alumnos_serializar = AlumnoSerializers(alumnos,many=True)
        else:
            alumnos = Alumno.objects.filter(rut=id)
            alumnos_serializar = ProfesorSerializers(alumnos,many=True)
        return JsonResponse(alumnos_serializar.data,safe=False)
    return JsonResponse("sin metodo",safe=False)

@csrf_exempt
def AsignaturaApi(request,id=0):
    if request.method=='GET':
        asignatura = Asignatura.objects.all()
        asignatura_serializers = AsignaturaSerializers(asignatura)
        return JsonResponse(asignatura_serializers.data,safe=False)

@csrf_exempt
def AsistenciaApi(request,id=0):
    if request.method=='PUT':
        asistencia_data =JSONParser().parse(request)
        asistencia = Asistencia.objects.get(fecha= asistencia_data['fecha'])
        asistencia_serializer= AsistenciaSerializers(asistencia,data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return JsonResponse('MensajeExito',safe=False)
        return JsonResponse('mensajeError',safe=False)
    if request.method=='POST':
        asistencia_data = JSONParser().parse(request)
        asistencia_serializer = AsistenciaSerializers(data=asistencia_data)
        if asistencia_serializer.is_valid():
            asistencia_serializer.save()
            return JsonResponse("Agregado",safe=False)
        return JsonResponse("No pudo agregar",safe=False)
    return JsonResponse("No encontro metodo",safe=False)


@csrf_exempt
def conteo_asistencias(request):
    if request.method=='POST':        
        cantidad = Asistencia.objects.all().count()
        return JsonResponse(cantidad,safe=False)
    return JsonResponse(0,safe=False)