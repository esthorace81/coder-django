# Problemas con los permisos de Windows

Si llegara a aparece un problema de permisos a la hora de activar el entorno virtual, intenta ejecutar en la terminal de `Microsoft PowerShell`:

    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser 

Reiniciar la terminal para que los cambios tengan efecto.

Si aún continúa, por única vez, abrir `Microsoft PowerShell` en modo **administrador**, y ejecutar el comando:

    Set-ExecutionPolicy Unrestricted

Reiniciar la terminal para que los cambios tengan efecto.
