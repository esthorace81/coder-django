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


def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😊 ✨ Ganaste ✨"
    else:
        mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😒 Sigue intentando. Presiona F5"

    datos = {
        "title": "Tiro de Dados",
        "message": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "core/dados.html", context=datos)
