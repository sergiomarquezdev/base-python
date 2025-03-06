"""
Introduction to Python Programming

This module provides an introduction to Python, explaining its
key features, benefits, and basic execution model.
"""

import sys
from typing import List


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


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    python_introduction()
