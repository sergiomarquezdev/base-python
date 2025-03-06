#!/usr/bin/env python3
"""
Python Fundamentals Cheatsheet

This file serves as a comprehensive reference for Python programming fundamentals,
covering basic to advanced concepts with practical examples.

Usage:
    Run the entire file to see all examples in action:
    $ python main.py

    Or import specific functions to use them in your own code:
    >>> from main import calculate_average
    >>> calculate_average([1, 2, 3, 4, 5])
    3.0
"""

import math
import random
import sys
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from functools import reduce
from collections import Counter, defaultdict

# --------------------------
# -- INTRODUCCIÓN A PYTHON --
# --------------------------

def python_introduction() -> None:
    """Display introduction to Python programming language.

    This function provides a brief overview of Python's key features and benefits.
    """
    print("\n=== INTRODUCCIÓN A PYTHON ===")

    # ¿Por qué aprender Python?
    print("\n-- ¿Por qué aprender Python? --")
    reasons = [
        "Sintaxis clara y legible",
        "Lenguaje multipropósito",
        "Gran comunidad y documentación",
        "Amplias bibliotecas y frameworks",
        "Alta demanda en el mercado laboral",
        "Fácil de aprender para principiantes"
    ]

    for i, reason in enumerate(reasons, 1):
        print(f"{i}. {reason}")

    # Primera aplicación
    print("\n-- Primera aplicación --")
    print('print("¡Hola, Mundo!")')
    print("\nResultado:")
    print("¡Hola, Mundo!")

    # Cómo se ejecuta el código
    print("\n-- Cómo se ejecuta el código --")
    print("1. El intérprete de Python lee el código")
    print("2. Compila a bytecode")
    print("3. La máquina virtual de Python (PVM) ejecuta el bytecode")
    print(f"4. La versión actual de Python es: {sys.version.split()[0]}")


# --------------------------
# -- TIPOS BÁSICOS --
# --------------------------

def basic_types() -> None:
    """Demonstrate basic data types in Python.

    Shows examples of variables, strings, numbers, and type conversion.
    """
    print("\n=== TIPOS BÁSICOS ===")

    # Variables
    print("\n-- Variables --")
    name = "Juan"
    age = 30
    height = 1.75
    is_student = True

    print(f"Nombre (str): {name}, tipo: {type(name)}")
    print(f"Edad (int): {age}, tipo: {type(age)}")
    print(f"Altura (float): {height}, tipo: {type(height)}")
    print(f"¿Es estudiante? (bool): {is_student}, tipo: {type(is_student)}")

    # Strings
    print("\n-- Strings --")
    greeting = "Hola, mundo!"
    multiline = """Este es un texto
que ocupa varias
líneas."""

    print(f"Saludo: {greeting}")
    print(f"Texto multilínea:\n{multiline}")

    # Formato de strings
    print("\n-- Formato de strings --")
    old_format = "Hola, me llamo %s y tengo %d años." % (name, age)
    format_method = "Hola, me llamo {} y tengo {} años.".format(name, age)
    f_string = f"Hola, me llamo {name} y tengo {age} años."

    print("1. Formato antiguo: " + old_format)
    print("2. Método format(): " + format_method)
    print("3. f-strings (3.6+): " + f_string)

    # Métodos de strings
    print("\n-- Métodos de strings --")
    text = "  python es increíble  "
    print(f"Original: '{text}'")
    print(f"upper(): '{text.upper()}'")
    print(f"capitalize(): '{text.capitalize()}'")
    print(f"strip(): '{text.strip()}'")
    print(f"replace(): '{text.replace('increíble', 'asombroso')}'")
    print(f"split(): {text.split()}")
    print(f"join(): {'_'.join(['python', 'es', 'genial'])}")
    print(f"find('py'): {text.find('py')}")

    # Secuencias de escape
    print("\n-- Secuencias de escape --")
    escape_examples = [
        r"Nueva línea: \n",
        r"Tabulación: \t",
        r"Comilla simple: \'",
        r"Comilla doble: \"",
        r"Barra invertida: \\"
    ]

    print("Ejemplos de secuencias de escape (mostradas en crudo):")
    for example in escape_examples:
        print(f"  {example}")

    print("\nCon interpretación:")
    print("Nueva línea: \nEjemplo")
    print("Tabulación: \tEjemplo")
    print("Comillas: \"Ejemplo\"")

    # Números
    print("\n-- Números --")
    integer = 42
    float_num = 3.14159
    complex_num = 1 + 2j

    print(f"Entero: {integer}, tipo: {type(integer)}")
    print(f"Decimal: {float_num}, tipo: {type(float_num)}")
    print(f"Complejo: {complex_num}, tipo: {type(complex_num)}")

    # Operaciones básicas
    print("\nOperaciones básicas:")
    print(f"Suma: 5 + 3 = {5 + 3}")
    print(f"Resta: 5 - 3 = {5 - 3}")
    print(f"Multiplicación: 5 * 3 = {5 * 3}")
    print(f"División: 5 / 3 = {5 / 3}")
    print(f"División entera: 5 // 3 = {5 // 3}")
    print(f"Módulo: 5 % 3 = {5 % 3}")
    print(f"Potencia: 5 ** 3 = {5 ** 3}")

    # Módulo math
    print("\n-- Módulo math --")
    print(f"math.pi: {math.pi}")
    print(f"math.sqrt(16): {math.sqrt(16)}")
    print(f"math.floor(3.7): {math.floor(3.7)}")
    print(f"math.ceil(3.7): {math.ceil(3.7)}")
    print(f"math.sin(math.pi/2): {math.sin(math.pi/2)}")

    # Conversión de tipos
    print("\n-- Conversión de tipos --")
    num_str = "42"
    num_float = "3.14"

    print(f"str a int: int('{num_str}') = {int(num_str)}")
    print(f"str a float: float('{num_float}') = {float(num_float)}")
    print(f"int a str: str({integer}) = '{str(integer)}'")
    print(f"float a int: int({float_num}) = {int(float_num)} (trunca el decimal)")
    print(f"bool de valor no-cero: bool({integer}) = {bool(integer)}")
    print(f"bool de cero: bool(0) = {bool(0)}")
    print(f"bool de string vacío: bool('') = {bool('')}")


# --------------------------
# -- CONTROL DE FLUJO --
# --------------------------

def flow_control() -> None:
    """Demonstrate flow control structures in Python.

    Covers comparisons, conditionals, loops, and logical operations.
    """
    print("\n=== CONTROL DE FLUJO ===")

    # Comparadores lógicos
    print("\n-- Comparadores lógicos --")
    print(f"Igual (==): 5 == 5 es {5 == 5}")
    print(f"Distinto (!=): 5 != 5 es {5 != 5}")
    print(f"Mayor que (>): 5 > 3 es {5 > 3}")
    print(f"Menor que (<): 5 < 3 es {5 < 3}")
    print(f"Mayor o igual (>=): 5 >= 5 es {5 >= 5}")
    print(f"Menor o igual (<=): 5 <= 3 es {5 <= 3}")
    print(f"Identidad (is): [] is [] es {[] is []}")
    print(f"No identidad (is not): 'a' is not 'b' es {'a' is not 'b'}")

    # if, else, elif
    print("\n-- if, else, elif --")
    x = 10

    print(f"Valor de x: {x}")
    print("Resultado de la condición:")

    if x > 15:
        print("x es mayor que 15")
    elif x > 5:
        print("x es mayor que 5 pero no mayor que 15")
    else:
        print("x es menor o igual a 5")

    # Operador ternario
    print("\n-- Operador ternario --")
    age = 20
    status = "adulto" if age >= 18 else "menor"
    print(f"Edad: {age}, Estado: {status}")

    # Operadores lógicos
    print("\n-- Operadores lógicos --")
    a, b = True, False
    print(f"a = {a}, b = {b}")
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"not a: {not a}")

    # Operaciones de corto-circuito
    print("\n-- Operaciones de corto-circuito --")
    print("En 'and', si el primer operando es False, el segundo no se evalúa")
    print("En 'or', si el primer operando es True, el segundo no se evalúa")

    # Cadena de comparadores
    print("\n-- Cadena de comparadores --")
    value = 15
    print(f"value = {value}")
    print(f"10 < value < 20: {10 < value < 20}")

    # for
    print("\n-- for --")
    print("Iterando sobre una lista:")
    fruits = ["manzana", "banana", "cereza"]
    for fruit in fruits:
        print(f"  - {fruit}")

    print("\nIterando sobre un rango:")
    for i in range(3):
        print(f"  - Índice: {i}")

    # for else
    print("\n-- for else --")
    print("Buscando un número par en una lista:")
    numbers = [1, 3, 5, 7, 8, 9]
    for num in numbers:
        if num % 2 == 0:
            print(f"  Encontrado número par: {num}")
            break
    else:
        print("  No se encontraron números pares")

    # Iterables
    print("\n-- Iterables --")
    print("Diferentes tipos de iterables:")
    print(f"  Lista: {list(range(3))}")
    print(f"  Tupla: {tuple(range(3))}")
    print(f"  Set: {set(range(3))}")
    print(f"  Dict: {dict([(i, i**2) for i in range(3)])}")
    print(f"  String: Iterar sobre 'abc' produce {[c for c in 'abc']}")

    # Loops anidados
    print("\n-- Loops anidados --")
    print("Tabla de multiplicación (3x3):")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"  {i} x {j} = {i * j}")

    # Ejercicio: Suma de los primeros n números pares
    print("\n-- Ejercicio: Suma de los primeros n números pares --")
    n = 5
    suma = sum(i * 2 for i in range(1, n + 1))
    print(f"La suma de los primeros {n} números pares es: {suma}")


# --------------------------
# -- FUNCIONES --
# --------------------------

def function_examples() -> None:
    """Demonstrate various aspects of functions in Python.

    Covers function definition, parameters, return values, and scope.
    """
    print("\n=== FUNCIONES ===")

    # Funciones básicas
    print("\n-- Funciones básicas --")

    def greet(name: str) -> str:
        """Return a greeting message for the given name.

        Args:
            name: The name to greet

        Returns:
            A greeting string
        """
        return f"¡Hola, {name}!"

    result = greet("María")
    print(f"Llamada a función greet('María'): {result}")
    print(f"Documentación de la función: {greet.__doc__}")

    # Parámetros y argumentos
    print("\n-- Parámetros y argumentos --")

    def describe_person(name: str, age: int) -> str:
        """Return a description of a person with their name and age.

        Args:
            name: The person's name
            age: The person's age

        Returns:
            A description string
        """
        return f"{name} tiene {age} años."

    print(f"describe_person('Ana', 25): {describe_person('Ana', 25)}")

    # Argumentos opcionales
    print("\n-- Argumentos opcionales --")

    def power(base: float, exponent: float = 2) -> float:
        """Calculate base raised to the power of exponent.

        Args:
            base: The base number
            exponent: The exponent (default: 2)

        Returns:
            The result of base^exponent
        """
        return base ** exponent

    print(f"power(4): {power(4)}")
    print(f"power(2, 3): {power(2, 3)}")

    # Argumentos nombrados
    print("\n-- Argumentos nombrados --")
    print(f"describe_person(age=30, name='Carlos'): {describe_person(age=30, name='Carlos')}")

    # *args
    print("\n-- *args --")

    def sum_all(*args: float) -> float:
        """Sum all the arguments provided.

        Args:
            *args: Variable number of numerical arguments

        Returns:
            The sum of all arguments
        """
        return sum(args)

    print(f"sum_all(1, 2, 3, 4): {sum_all(1, 2, 3, 4)}")

    # **kwargs
    print("\n-- **kwargs --")

    def person_info(**kwargs: Any) -> str:
        """Format person information from keyword arguments.

        Args:
            **kwargs: Arbitrary keyword arguments

        Returns:
            A formatted string with the person's information
        """
        info = []
        for key, value in kwargs.items():
            info.append(f"{key}: {value}")
        return ", ".join(info)

    print(f"person_info(nombre='Laura', edad=28, profesión='ingeniera'): "
          f"{person_info(nombre='Laura', edad=28, profesion='ingeniera')}")

    # return
    print("\n-- return --")

    def calculate_statistics(numbers: List[float]) -> Tuple[float, float, float]:
        """Calculate basic statistics for a list of numbers.

        Args:
            numbers: A list of numbers

        Returns:
            A tuple containing (minimum, maximum, average)
        """
        if not numbers:
            return 0, 0, 0
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    data = [5, 2, 9, 1, 7]
    min_val, max_val, avg = calculate_statistics(data)
    print(f"Para los datos {data}:")
    print(f"  Mínimo: {min_val}, Máximo: {max_val}, Promedio: {avg}")

    # Alcance (Scope)
    print("\n-- Alcance (Scope) --")

    global_var = "variable global"

    def demonstrate_scope() -> None:
        """Demonstrate variable scope in Python."""
        local_var = "variable local"
        print(f"  Dentro de la función - global_var: {global_var}")
        print(f"  Dentro de la función - local_var: {local_var}")

    demonstrate_scope()
    print(f"  Fuera de la función - global_var: {global_var}")
    try:
        print(f"  Fuera de la función - local_var: {local_var}")
    except NameError as e:
        print(f"  Error al acceder a local_var: {e}")

    # Ejercicio: Función para verificar si un número es primo
    print("\n-- Ejercicio: Verificar si un número es primo --")

    def is_prime(n: int) -> bool:
        """Check if a number is prime.

        Args:
            n: The number to check

        Returns:
            True if n is prime, False otherwise
        """
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    number = 17
    print(f"¿Es {number} un número primo? {is_prime(number)}")


# --------------------------
# -- TIPOS AVANZADOS --
# --------------------------

def advanced_types() -> None:
    """Demonstrate advanced data types in Python.

    Covers lists, tuples, sets, dictionaries, and related operations.
    """
    print("\n=== TIPOS AVANZADOS ===")

    # Listas
    print("\n-- Listas --")
    fruits = ["manzana", "banana", "cereza", "dátil"]
    print(f"Lista de frutas: {fruits}")
    print(f"Primera fruta: {fruits[0]}")
    print(f"Última fruta: {fruits[-1]}")
    print(f"Rebanado (slicing) [1:3]: {fruits[1:3]}")

    # Manipulando listas
    print("\n-- Manipulando listas --")
    numbers = [3, 1, 4, 1, 5, 9]
    print(f"Lista original: {numbers}")

    # Modificación
    numbers[0] = 10
    print(f"Después de numbers[0] = 10: {numbers}")

    # Métodos de listas
    numbers.append(2)
    print(f"Después de append(2): {numbers}")

    numbers.insert(1, 20)
    print(f"Después de insert(1, 20): {numbers}")

    popped = numbers.pop()
    print(f"Después de pop(): {numbers}, valor extraído: {popped}")

    numbers.remove(1)  # Elimina la primera ocurrencia de 1
    print(f"Después de remove(1): {numbers}")

    numbers.sort()
    print(f"Después de sort(): {numbers}")

    numbers.reverse()
    print(f"Después de reverse(): {numbers}")

    # Desempaquetar listas
    print("\n-- Desempaquetar listas --")
    coordinates = [10, 20, 30]
    x, y, z = coordinates
    print(f"coordinates = {coordinates}")
    print(f"x = {x}, y = {y}, z = {z}")

    # Desempaquetado con asterisco
    first, *rest = [1, 2, 3, 4, 5]
    print(f"first = {first}, rest = {rest}")

    # Iterando listas
    print("\n-- Iterando listas --")
    animals = ["perro", "gato", "conejo"]

    print("Usando for:")
    for animal in animals:
        print(f"  - {animal}")

    print("\nUsando enumerate():")
    for i, animal in enumerate(animals, 1):
        print(f"  {i}. {animal}")

    # Buscando elementos
    print("\n-- Buscando elementos --")
    letters = ["a", "b", "c", "b", "d"]
    print(f"letters = {letters}")
    print(f"'b' in letters: {'b' in letters}")
    print(f"index de 'b': {letters.index('b')}")
    print(f"count de 'b': {letters.count('b')}")

    # Agregando y eliminando
    print("\n-- Agregando y eliminando --")
    colors = ["rojo", "verde"]
    print(f"Lista original: {colors}")

    colors.extend(["azul", "amarillo"])
    print(f"Después de extend(): {colors}")

    # Usando slices para modificar
    colors[1:3] = ["púrpura", "naranja", "rosa"]
    print(f"Después de slice assignment: {colors}")

    # Ordenando listas
    print("\n-- Ordenando listas --")
    scores = [82, 65, 93, 45, 78]
    print(f"Puntuaciones originales: {scores}")

    # sorted() crea una nueva lista
    sorted_scores = sorted(scores)
    print(f"sorted(scores): {sorted_scores}")

    # Orden descendente
    desc_scores = sorted(scores, reverse=True)
    print(f"sorted(scores, reverse=True): {desc_scores}")

    # Ordenamiento personalizado
    words = ["zanahoria", "manzana", "pera", "kiwi"]
    print(f"Palabras: {words}")

    # Ordenar por longitud
    sorted_by_length = sorted(words, key=len)
    print(f"Ordenadas por longitud: {sorted_by_length}")

    # Expresiones lambda
    print("\n-- Expresiones lambda --")
    print("Lambda para duplicar: lambda x: x * 2")
    duplicar = lambda x: x * 2
    print(f"duplicar(5) = {duplicar(5)}")

    # Ordenar con lambda
    people = [("Juan", 25), ("Ana", 22), ("Carlos", 30)]
    print(f"Lista de personas: {people}")

    # Ordenar por edad
    sorted_by_age = sorted(people, key=lambda person: person[1])
    print(f"Ordenadas por edad: {sorted_by_age}")

    # Listas de comprensión
    print("\n-- Listas de comprensión --")

    # Forma tradicional
    squares_traditional = []
    for i in range(1, 6):
        squares_traditional.append(i**2)
    print(f"Cuadrados (tradicional): {squares_traditional}")

    # Con comprensión de lista
    squares_comprehension = [i**2 for i in range(1, 6)]
    print(f"Cuadrados (comprensión): {squares_comprehension}")

    # Con condición
    even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
    print(f"Cuadrados de números pares: {even_squares}")

    # map y filter
    print("\n-- map y filter --")
    numbers = [1, 2, 3, 4, 5]

    # map con función lambda
    doubled = list(map(lambda x: x * 2, numbers))
    print(f"map (duplicar): {doubled}")

    # filter con función lambda
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"filter (pares): {evens}")

    # Tuplas
    print("\n-- Tuplas --")
    point = (10, 20)
    print(f"Tupla: {point}")
    print(f"x = {point[0]}, y = {point[1]}")

    # Tuplas vs listas
    print("\nTuplas vs listas:")
    print("- Las tuplas son inmutables (no se pueden modificar)")
    print("- Las tuplas suelen usarse para datos que no cambiarán")
    print("- Las tuplas pueden usarse como claves de diccionarios")

    # Tupla de un solo elemento
    single_item_tuple = (42,)  # La coma es necesaria
    print(f"Tupla de un elemento: {single_item_tuple}")

    # Sets
    print("\n-- Sets --")
    fruits_set = {"manzana", "banana", "cereza", "manzana"}  # Nótese el duplicado
    print(f"Set: {fruits_set}")  # Los duplicados se eliminan automáticamente

    # Operaciones con sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print(f"set_a = {set_a}")
    print(f"set_b = {set_b}")
    print(f"Unión: {set_a | set_b}")
    print(f"Intersección: {set_a & set_b}")
    print(f"Diferencia: {set_a - set_b}")
    print(f"Diferencia simétrica: {set_a ^ set_b}")

    # Métodos de sets
    colors = {"rojo", "verde", "azul"}
    print(f"\nSet original: {colors}")

    colors.add("amarillo")
    print(f"Después de add(): {colors}")

    colors.remove("verde")  # Lanza error si no existe
    print(f"Después de remove(): {colors}")

    colors.discard("negro")  # No lanza error si no existe
    print(f"Después de discard(): {colors}")

    # Diccionarios
    print("\n-- Diccionarios --")
    person = {
        "nombre": "Elena",
        "edad": 28,
        "profesión": "ingeniera",
        "hobbies": ["lectura", "natación", "fotografía"]
    }

    print(f"Diccionario persona: {person}")

    # Accediendo a valores
    print(f"Nombre: {person['nombre']}")
    print(f"Edad: {person['edad']}")

    # get() con valor por defecto
    print(f"Ciudad: {person.get('ciudad', 'No especificada')}")

    # Modificando el diccionario
    person["edad"] = 29
    person["ciudad"] = "Madrid"

    print(f"Diccionario actualizado: {person}")

    # Iterando sobre diccionarios
    print("\nClaves:")
    for key in person.keys():
        print(f"  - {key}")

    print("\nValores:")
    for value in person.values():
        print(f"  - {value}")

    print("\nPares clave-valor:")
    for key, value in person.items():
        print(f"  - {key}: {value}")

    # Diccionarios por comprensión
    print("\nDiccionario por comprensión:")
    squares_dict = {i: i**2 for i in range(1, 6)}
    print(f"Cuadrados: {squares_dict}")

    # Operador de desempaquetamiento
    print("\n-- Operador de desempaquetamiento --")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Unir diccionarios
    combined = {**dict1, **dict2}
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    print(f"combined: {combined}")

    # Desempaquetar listas
    combined_list = [*range(3), *range(5, 8)]
    print(f"Lista combinada: {combined_list}")


# --------------------------
# -- PUNTO DE ENTRADA PRINCIPAL --
# --------------------------

def main() -> None:
    """Main entry point of the application.

    Execute all example functions to demonstrate Python concepts.
    """
    print("=" * 50)
    print("      PYTHON: GUÍA PRÁCTICA DE REFERENCIA")
    print("=" * 50)

    # Ejecutar todas las funciones de ejemplo
    python_introduction()
    basic_types()
    flow_control()
    function_examples()
    advanced_types()

    print("\n" + "=" * 50)
    print("      FIN DE LA GUÍA")
    print("=" * 50)


if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el script se ejecuta directamente,
    no cuando se importa como módulo.
    """
    main()
