from django.shortcuts import render
from django.views.generic import ListView, CreateView

from Agrodigital.models import *

def home(request):
    return render(request, "index.html")

def planes(request):
    return render(request, "planesdeaccion.html")


class vistapreguntas(CreateView):
    template_name = "preguntas.html"
    model = encuesta
    fields = "__all__"
    success_url = "/"

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





