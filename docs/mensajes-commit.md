# Convenciones de mensajes de commit

Tener convenciones para los mensajes de commit es fundamental porque:

- Mejora la claridad: Los mensajes uniformes permiten entender rápidamente qué cambios se hicieron y por qué.

- Facilita la colaboración: Ayuda a otros desarrolladores a interpretar el historial de commits de forma consistente.

- Optimiza el uso de herramientas: Herramientas como git log o integraciones CI/CD se benefician de mensajes estructurados, mejorando la trazabilidad.

- Evita ambigüedades: Reduce la confusión sobre la intención de los cambios.

## Comventional Commits

`Conventional Commits` es un estándar ampliamente adoptado para escribir mensajes de commits estructurados. Su formato es:

`<tipo>[opcional(scope)]: <mensaje corto>`

1. Tipo (obligatorio): Describe el propósito del cambio. Ejemplos comunes:

    **feat**: una nueva funcionalidad

    **fix**: corrección de un error

    **docs**: cambios en la documentación

    **style**: cambios relacionados con el formato (sin impacto en el código)

    **refactor**: cambios que mejoran el código sin cambiar funcionalidad

    **test**: añadir o actualizar pruebas

    **chore**: tareas de mantenimiento que no afectan el código fuente o pruebas (por ejemplo, actualizaciones de dependencias).

2. Scope (opcional): Especifica qué parte del proyecto se modifica. Se coloca entre paréntesis. Ejemplo: feat(api):.

3. Mensaje corto (obligatorio): Una descripción breve y concisa del cambio, en tiempo presente y en minúsculas.

4. Mensaje extendido (opcional): Si es necesario, se puede añadir más contexto después de una línea en blanco (no en el título).
