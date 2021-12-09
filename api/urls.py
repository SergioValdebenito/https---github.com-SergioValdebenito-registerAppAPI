
from api import views
from django.conf.urls import url

from rest_framework.urlpatterns  import format_suffix_patterns


urlpatterns=[
    url(r'^api/persona/$',views.PersonaViewSet.as_view()),
    url(r'^api/persona_buscar/(?P<rut>.+)$', views.PersonaBuscarViewSet.as_view()),
    url(r'^api/asignatura/$',views.AsignaturaViewSet.as_view()),
    url(r'^api/asistencia/$',views.AsistenciaViewSet.as_view()),
    url(r'^api/asignatura_api/$',views.AsignaturaApi),
    url(r'^api/asistencia_api/$',views.AsistenciaApi),
    url(r'^api/profe/(?P<id>.+)$',views.ProfesorApi),
    url(r'^api/alumno/(?P<id>.+)$',views.AlumnoApi),
    url(r'^api/profe_curso/(?P<rutp>.+)$',views.CursoProfesorBuscarViewSet.as_view()),
    url(r'^api/asistencia_listar/$',views.AsistenciaListarViewSet.as_view()),
    url(r'^api/conteo/$',views.conteo_asistencias),
]
urlpatterns = format_suffix_patterns(urlpatterns)


