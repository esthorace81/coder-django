from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola desde Django!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")
