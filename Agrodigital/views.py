from django.shortcuts import render
from django.views.generic import ListView, CreateView

from Agrodigital.models import *

def home(request):
    return render(request, "index.html")

def planes(request):
    return render(request, "planesdeaccion.html")

class listapreguntas(CreateView):
    template_name = "preguntas.html"
    model = encuesta
    fields = "__all__"
    success_url = "/"

class resultadospreguntas(ListView):
    template_name = "respuesta.html"
    model = encuesta
    fields = ["p1_dim1", "p2_dim1", "p3_dim1", "p1_dim2","p2_dim2", "p3_dim2", "p4_dim2", "p5_dim2", "p6_dim2", "p1_dim3", "p2_dim3", "p3_dim3", "p4_dim3", "p1_dim4", "p2_dim4", "p3_dim4", "p4_dim4",
              "p1_dim5", "p2_dim5", "p3_dim5", "p4_dim5"]
    success_url = "/"

class vistapreguntas(ListView):
    template_name = "respuesta_final.html"
    context_object_name =  "Respuesta"

    def get_queryset(self):
        dim=self.kwargs['pk']
        lista=encuesta.objects.filter(
            id()
        )
        return lista

def p1accion1(request):
    return render(request, "plan1dim1.html")

def p2accion1(request):
    return render(request, "plan2dim1.html")

def p3accion1(request):
    return render(request, "plan3dim1.html")

def p4accion1(request):
    return render(request, "plan4dim1.html")

def p1accion2(request):
    return render(request, "plan1dim2.html")

def p2accion2(request):
    return render(request, "plan2dim2.html")

def p3accion2(request):
    return render(request, "plan3dim2.html")

def p4accion2(request):
    return render(request, "plan4dim2.html")

def p1accion3(request):
    return render(request, "plan1dim3.html")

def p2accion3(request):
    return render(request, "plan2dim3.html")

def p3accion3(request):
    return render(request, "plan3dim3.html")

def p4accion3(request):
    return render(request, "plan4dim3.html")

def p1accion4(request):
    return render(request, "plan1dim4.html")

def p2accion4(request):
    return render(request, "plan2dim4.html")

def p3accion4(request):
    return render(request, "plan3dim4.html")

def p4accion4(request):
    return render(request, "plan4dim4.html")

def p1accion5(request):
    return render(request, "plan1dim5.html")

def p2accion5(request):
    return render(request, "plan2dim5.html")

def p3accion5(request):
    return render(request, "plan3dim5.html")

def p4accion5(request):
    return render(request, "plan4dim5.html")





