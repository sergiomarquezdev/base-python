"""
Basic Data Types in Python

This module covers Python's basic data types, including
variables, strings, numbers, and type conversion.
"""

import math
from typing import Any


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


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    basic_types()
