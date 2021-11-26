from django.urls import path

from Agrodigital.views import *
from Agrodigital import views

urlpatterns = [
    path('inicio/', home,name="inicio"),
    path('preguntas/', views.listapreguntas.as_view(), name="encuesta"),
    path('puntajes/', views.resultadospreguntas.as_view(), name="resultado"),
    path('respuesta/<pk>/', views.vistapreguntas.as_view(), name="formulariorespondido"),
    path('p1dim1/', p1accion1, name="principiante-intermediodim1"),
    path('p2dim1/', p2accion1, name="intermedio-experimentadodim1"),
    path('p3dim1/', p3accion1, name="experimentado-expertodim1"),
    path('p4dim1/', p4accion1, name="experto-liderdim1"),
    path('p1dim2/', p1accion2, name="principiante-intermediodim2"),
    path('p2dim2/', p2accion2, name="intermedio-experimentadodim2"),
    path('p3dim2/', p3accion2, name="experimentado-expertodim2"),
    path('p4dim2/', p4accion2, name="experto-liderdim2"),
    path('p1dim3/', p1accion3, name="principiante-intermediodim3"),
    path('p2dim3/', p2accion3, name="intermedio-experimentadodim3"),
    path('p3dim3/', p3accion3, name="experimentado-expertodim3"),
    path('p4dim3/', p4accion3, name="experto-liderdim3"),
    path('p1dim4/', p1accion4, name="principiante-intermediodim4"),
    path('p2dim4/', p2accion4, name="intermedio-experimentadodim4"),
    path('p3dim4/', p3accion4, name="experimentado-expertodim4"),
    path('p4dim4/', p4accion4, name="experto-liderdim4"),
    path('p1dim5/', p1accion5, name="principiante-intermediodim5"),
    path('p2dim5/', p2accion5, name="intermedio-experimentadodim5"),
    path('p3dim5/', p3accion5, name="experimentado-expertodim5"),
    path('p4dim5/', p4accion5, name="experto-liderdim5"),

]
