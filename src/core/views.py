from django.http import HttpResponse
from django.shortcuts import render


def saludar(request):
    return HttpResponse("Hola desde Django!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()  # Capitaliza la primera letra del nombre
    apellido = apellido.capitalize()  # Capitaliza la primera letra del apellido
    return HttpResponse(f"Hola {nombre} {apellido} desde Django con parámetros!")


def index(request):
    from datetime import datetime

    año_actual = datetime.now().year
    contexto = {"año": año_actual}
    return render(request, "core/index.html", contexto)
