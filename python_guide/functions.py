"""
Functions in Python

This module demonstrates various aspects of functions in Python,
including definition, parameters, return values, and scope.
"""

from typing import Any, List, Tuple


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


# Funciones exportables para ser utilizadas por otros módulos
def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: A list of numbers

    Returns:
        The average value, or 0 if the list is empty
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n

    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    function_examples()

    # Demostración de las funciones exportables
    print("\n-- Demostración de funciones exportables --")
    print(f"calculate_average([1, 2, 3, 4, 5]): {calculate_average([1, 2, 3, 4, 5])}")
    print(f"factorial(5): {factorial(5)}")
