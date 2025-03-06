"""
Flow Control in Python

This module demonstrates flow control structures in Python,
including comparisons, conditionals, loops, and logical operations.
"""

from typing import List, Any


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


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    flow_control()
