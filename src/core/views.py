# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegisterForm

# from .models import Cliente


def index(request):
    return render(request, "core/index.html")


def about(request):
    return render(request, "core/about.html")


class MiLoginView(LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
    next_page = reverse_lazy("core:index")

    def form_valid(self, form):
        usuario = form.get_user()
        messages.success(self.request, f"Inicio de sesión exitoso. ¡Bienvenido {usuario.username}!")
        return super().form_valid(form)


class MiRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")

    def form_valid(self, form):
        messages.success(self.request, f"Registro exitoso. Ahora puedes iniciar sesión")
        return super().form_valid(form)


# def saludar(request):
#     return HttpResponse("Hola desde Django!")

# def saludar_con_etiqueta(request):
#     return HttpResponse("<h1>Hola desde Django con etiquetas!</h1>")

# def saludar_con_parametros(request, nombre: str, apellido: str):
#     nombre = nombre.capitalize()  # Capitaliza la primera letra del nombre
#     apellido = apellido.capitalize()  # Capitaliza la primera letra del apellido
#     return HttpResponse(f"Hola {nombre} {apellido} desde Django con parámetros!")

# def tirar_dado(request):
#     from datetime import datetime
#     from random import randint

#     tiro_de_dado = randint(1, 6)

#     if tiro_de_dado == 6:
#         mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😊 ✨ Ganaste ✨"
#     else:
#         mensaje = f"Has tirado el 🎲 y has sacado ¡{tiro_de_dado}! 😒 Sigue intentando. Presiona F5"

#     datos = {
#         "title": "Tiro de Dados",
#         "message": mensaje,
#         "fecha": datetime.now().strftime("%H:%M:%S.%f"),
#     }
#     return render(request, "core/dados.html", context=datos)


# def ejercicio_1(request):
#     nombre = "Louis"
#     apellido = "Van Beethoven"
#     return render(request, "core/ejercicio1.html", {"nombre": nombre, "apellido": apellido})


# def ver_notas(request):
#     lista_notas = [10, 8, 9, 7, 6, 8, 10]
#     return render(request, "core/notas.html", {"notas": lista_notas})


# def ejercicio_2(request):
#     usuarios = [
#         {"nombre": "Juan", "email": "juan@example.com"},
#         {"nombre": "María", "email": "maria@example.com"},
#         {"nombre": "Pedro", "email": "pedro@example.com"},
#     ]
#     return render(request, "core/ejercicio2.html", {"usuarios": usuarios})


# def cliente_list(request):
#     clientes = Cliente.objects.all()
#     return render(request, "core/cliente_list.html", {"clientes": clientes})
