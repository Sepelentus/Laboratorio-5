from http.client import HTTPResponse
from re import template
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    #titulo = " <h1>Esta es la seccion de Pagina Principal </h1> <br> <hr> <ul> <li><a href=http://127.0.0.1:8000> Home </a> </li> <li><a href=http://127.0.0.1:8000/carreras/> Carreras </a> </li> <li><a href=http://127.0.0.1:8000/docentes/> Docentes </a> </li> </ul> <br> <hr> <p> Lorem </p>"
    #return HttpResponse(titulo)
    return render(request, "core/home.html")
def carreras(request):
    #titulo = " <h1>Esta es la seccion de Carreras </h1> <br> <hr> <ul> <li><a href=http://127.0.0.1:8000> Home </a> </li> <li><a href=http://127.0.0.1:8000/carreras/> Carreras </a> </li> <li><a href=http://127.0.0.1:8000/docentes/> Docentes </a> </li> </ul> <br> <hr> <p> Lorem </p>"
    #return HttpResponse(titulo)
    return render(request, "core/carreras.html")
def docentes(request):
    #titulo = " <h1>Esta es la seccion de Docentes </h1> <br> <hr> <ul> <li><a href=http://127.0.0.1:8000> Home </a> </li> <li><a href=http://127.0.0.1:8000/carreras/> Carreras </a> </li> <li><a href=http://127.0.0.1:8000/docentes/> Docentes </a> </li> </ul> <br> <hr> <p> Lorem </p>"
    #return HttpResponse(titulo)
    return render(request, "core/docentes.html")
# Se importa HttpResponse y se escribe el def (nombre)(request) y luego http response