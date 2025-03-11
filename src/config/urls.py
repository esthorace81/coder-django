"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

# from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("productos/", include("producto.urls")),
    # path("saludar/", views.saludar),
    # path("saludar2/", views.saludar_con_etiqueta),
    # path("saludar3/<str:nombre>/<str:apellido>/", views.saludar_con_parametros),
    # path("", views.index),
    # path("tirar-dado/", views.tirar_dado),
    # path("ejercicio-1/", views.ejercicio_1),
    # path("ver-notas/", views.ver_notas),
    # path("ejercicio-2/", views.ejercicio_2),
    # path("cliente/", views.cliente_list),
]
