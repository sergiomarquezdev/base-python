# Python Fundamentals Guide

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)

Una guía práctica y completa para aprender Python desde los conceptos básicos hasta temas avanzados. Este proyecto está diseñado como un recurso educativo interactivo que permite a los usuarios explorar los fundamentos de Python ejecutando ejemplos prácticos.

## 📋 Tabla de Contenidos

- [Visión General](#visión-general)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
  - [Ejecutar toda la guía](#ejecutar-toda-la-guía)
  - [Ejecutar secciones específicas](#ejecutar-secciones-específicas)
  - [Uso como módulo](#uso-como-módulo)
- [Temas Cubiertos](#temas-cubiertos)
- [Contribuciones](#contribuciones)

## 🔍 Visión General

Esta guía proporciona ejemplos prácticos y explicaciones detalladas de los conceptos fundamentales de Python. Cada tema está organizado en módulos independientes que pueden ejecutarse por separado, lo que permite un aprendizaje progresivo y personalizado.

## 📁 Estructura del Proyecto

El proyecto está organizado en módulos temáticos para facilitar el aprendizaje y la navegación:

```
base-python/
│
├── main.py                 # Punto de entrada principal
├── README.md               # Este archivo
│
└── python_guide/          # Paquete principal
    ├── __init__.py         # Inicializador del paquete
    ├── introduction.py     # Introducción a Python
    ├── basic_types.py      # Tipos básicos (variables, strings, números)
    ├── flow_control.py     # Control de flujo (if, for, while)
    ├── functions.py        # Funciones y su uso
    ├── advanced_types.py   # Tipos avanzados (listas, tuplas, sets, diccionarios)
    ├── exception_handling.py # Manejo de excepciones y context managers
    ├── object_oriented.py  # Programación orientada a objetos
    ├── decorators.py       # Decoradores y funciones de orden superior
    └── concurrency.py      # Concurrencia y paralelismo
```

## 📋 Requisitos

- Python 3.10 o superior
- Entorno virtual (venv) recomendado
- Paquetes adicionales para ejemplos avanzados:
  - `requests` (para ejemplos de concurrencia)

## 🔧 Instalación

1. Clone el repositorio o descargue los archivos:

   ```bash
   git clone <url-del-repositorio>
   cd base-python
   ```

2. Cree y active un entorno virtual:

   ```bash
   # Crear el entorno virtual
   python -m venv venv

   # Activar en Windows
   venv\Scripts\activate

   # Activar en macOS/Linux
   source venv/bin/activate
   ```

3. Instale las dependencias necesarias:
   ```bash
   pip install requests
   ```

## 🚀 Uso

### Ejecutar toda la guía

Para ejecutar todos los ejemplos de la guía:

```bash
python main.py
```

### Ejecutar secciones específicas

Para ejecutar solo una sección específica de la guía, utilice el argumento `--section`:

| Sección               | Comando                                       |
| --------------------- | --------------------------------------------- |
| Introducción          | `python main.py --section introduction`       |
| Tipos básicos         | `python main.py --section basic_types`        |
| Control de flujo      | `python main.py --section flow_control`       |
| Funciones             | `python main.py --section functions`          |
| Tipos avanzados       | `python main.py --section advanced_types`     |
| Manejo de excepciones | `python main.py --section exception_handling` |
| Programación OO       | `python main.py --section object_oriented`    |
| Decoradores           | `python main.py --section decorators`         |
| Concurrencia          | `python main.py --section concurrency`        |

### Uso como módulo

También puede importar funciones específicas de la guía para usarlas en su propio código:

```python
# Ejemplos de importación y uso de funciones exportadas

# 1. Funciones básicas
from python_guide.functions import calculate_average
result = calculate_average([1, 2, 3, 4, 5])
print(result)  # Salida: 3.0

# 2. Tipos avanzados
from python_guide.advanced_types import merge_dictionaries
combined = merge_dictionaries({"a": 1}, {"b": 2})
print(combined)  # Salida: {'a': 1, 'b': 2}

# 3. Decoradores
from python_guide.decorators import debug
@debug
def add(a, b):
    return a + b
add(5, 3)  # Mostrará información de depuración

# 4. Concurrencia
from python_guide.concurrency import run_in_thread
def task():
    print("Tarea ejecutada en un hilo separado")
thread = run_in_thread(task)
thread.join()
```

## 📚 Temas Cubiertos

<details>
<summary><strong>Introducción a Python</strong></summary>

- ¿Por qué aprender Python?
- Primera aplicación
- Cómo se ejecuta el código
</details>

<details>
<summary><strong>Tipos Básicos</strong></summary>

- Variables
- Strings y sus métodos
- Formato de strings
- Secuencias de escape
- Números y operaciones
- Módulo math
- Conversión de tipos
</details>

<details>
<summary><strong>Control de Flujo</strong></summary>

- Comparadores lógicos
- Estructuras condicionales (if, else, elif)
- Operador ternario
- Operadores lógicos
- Bucles for y while
- Iterables
- Loops anidados
</details>

<details>
<summary><strong>Funciones</strong></summary>

- Definición de funciones
- Parámetros y argumentos
- Argumentos opcionales y nombrados
- \*args y \*\*kwargs
- Valores de retorno
- Alcance de variables
- Docstrings y anotaciones de tipo
</details>

<details>
<summary><strong>Tipos Avanzados</strong></summary>

- Listas y operaciones
- Desempaquetado de listas
- Expresiones lambda
- Listas de comprensión
- map, filter y reduce
- Tuplas
- Sets y sus operaciones
- Diccionarios
- Operador de desempaquetamiento
</details>

<details>
<summary><strong>Manejo de Excepciones</strong></summary>

- Bloques try/except/else/finally
- Captura de múltiples excepciones
- Lanzamiento de excepciones con raise
- Creación de excepciones personalizadas
- Context managers (with)
- Patrones de manejo de errores
</details>

<details>
<summary><strong>Programación Orientada a Objetos</strong></summary>

- Clases y objetos
- Herencia
- Encapsulación
- Polimorfismo
- Métodos especiales (dunder methods)
- Propiedades (@property)
- Métodos de clase y estáticos
- Clases abstractas
- Dataclasses
</details>

<details>
<summary><strong>Decoradores</strong></summary>

- Funciones como objetos de primera clase
- Closures
- Decoradores básicos
- Decoradores con argumentos
- Múltiples decoradores
- Decoradores de clase
- Aplicaciones prácticas (timing, caching, validación)
</details>

<details>
<summary><strong>Concurrencia y Paralelismo</strong></summary>

- Threading para tareas I/O-bound
- Multiprocessing para tareas CPU-bound
- AsyncIO para programación asíncrona
- concurrent.futures
- Patrones de concurrencia
- Comunicación entre procesos/hilos
- Sincronización
</details>

## 👥 Contribuciones

Las contribuciones son bienvenidas. Si encuentra errores o desea agregar más ejemplos, siéntase libre de abrir un issue o enviar un pull request.
