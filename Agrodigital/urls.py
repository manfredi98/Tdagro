from django.urls import path

from Agrodigital.views import *
from Agrodigital import views

urlpatterns = [
    path('inicio/', home,name="inicio"),
    path('preguntas/', views.listapreguntas.as_view(), name="listapreguntas"  ),
    path('p1dim1/', p1accion1, name="plandeaccion"),
    path('p2dim1/', p2accion1, name="plandeaccion"),
    path('p3dim1/', p3accion1, name="plandeaccion"),
    path('p4dim1/', p4accion1, name="plandeaccion"),
    path('p1dim2/', p1accion2, name="plandeaccion"),
    path('p2dim2/', p2accion2, name="plandeaccion"),
    path('p3dim2/', p3accion2, name="plandeaccion"),
    path('p4dim2/', p4accion2, name="plandeaccion"),
    path('p1dim3/', p1accion3, name="plandeaccion"),
    path('p2dim3/', p2accion3, name="plandeaccion"),
    path('p3dim3/', p3accion3, name="plandeaccion"),
    path('p4dim3/', p4accion3, name="plandeaccion"),
    path('p1dim4/', p1accion4, name="plandeaccion"),
    path('p2dim4/', p2accion4, name="plandeaccion"),
    path('p3dim4/', p3accion4, name="plandeaccion"),
    path('p4dim4/', p4accion4, name="plandeaccion"),
    path('p1dim5/', p1accion5, name="plandeaccion"),
    path('p2dim5/', p2accion5, name="plandeaccion"),
    path('p3dim5/', p3accion5, name="plandeaccion"),
    path('p4dim5/', p4accion5, name="plandeaccion"),

]
