# Django

## Crear un proyecto

    mkdir src
    cd src
    django-admin startproject config .

## Comprobar posibles problemas en el proyecto

    python manage.py check

## Ejecutar el servidor

    python manage.py runserver

## Crear una aplicación

    python manage.py startapp app

## Preparar archivos de migración

    python manage.py makemigrations

## Aplicar migraciones a la base de datos

    python manage.py migrate

## Shell interactivo con las configuraciones de Django

    python manage.py shell

## Crear superusuario

    python manage.py createsuperuser