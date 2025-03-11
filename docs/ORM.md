# ORM de Django

## Crear registros

```py
from app.models import Modelo
objeto = Modelo(campo1="valor", campo2="valor")
objeto.save()  # Guarda el objeto en la base de datos
```

## Obtener registros

```py
Modelo.objects.all()  # Devuelve todos los registros
Modelo.objects.get(id=valor)  # Devuelve un único registro por ID
```

## Actualizar registros

```py
objeto = Modelo.objects.get(id=valor)
objeto.campo = "nuevo_valor"
objeto.save()
```

## Eliminar registros

```py
objeto = Modelo.objects.get(id=valor)
objeto.delete()
```

## Filtrar consultas

### Cadenas

```py
Modelo.objects.filter(campo="valor")
Modelo.objects.filter(campo__contains="subcadena")
Modelo.objects.filter(campo__startswith="inicio")
Modelo.objects.filter(campo__endswith="final")
```

### Comparaciones

```py
Modelo.objects.filter(id__in=[1, 2, 3])
Modelo.objects.filter(id__gt=3)  # Mayor que
Modelo.objects.filter(id__gte=3)  # Mayor o igual que
Modelo.objects.filter(id__lt=2)  # Menor que
Modelo.objects.filter(id__lte=2)  # Menor o igual que
```

### Fechas

```py
from datetime import date
Modelo.objects.filter(fecha__year=2024)
Modelo.objects.filter(fecha__month=8)
Modelo.objects.filter(fecha__day=1)
Modelo.objects.filter(fecha__gt=date(2022, 1, 1))
```

### Relaciones

```py
Modelo.objects.filter(campo_relacionado__campo="valor")
```

### Operaciones lógicas (Q objects)

```py
from django.db.models import Q
Modelo.objects.filter(Q(expresión) | Q(expresión))  # OR
Modelo.objects.filter(Q(expresión) & Q(expresión))  # AND
Modelo.objects.filter(~Q(expresión))  # NOT
Modelo.objects.filter(Q(expresión) | Q(expresión)).distinct()  # Evita duplicados
```

## Funciones de agregación

```py
from django.db.models import Count, Avg, Max, Min, Sum

Modelo.objects.aggregate(Count('campo'))
Modelo.objects.aggregate(Avg('campo'))
```

## Ordenar

```py
Modelo.objects.order_by('campo')  # Ascendente
Modelo.objects.order_by('-campo')  # Descendente
```

## Limitar resultados

```py
Modelo.objects.all()[:10]  # Primeros 10 registros
Modelo.objects.all()[5:15]  # Registros del 5 al 14
```
