"""
Exception Handling in Python

This module demonstrates exception handling in Python,
including try/except blocks, custom exceptions, and context managers.
"""

import os
import sys
from typing import Any, List, Dict, Optional, Union, TextIO


def exception_handling() -> None:
    """Demonstrate exception handling techniques in Python.

    Covers try/except/else/finally blocks, built-in exceptions,
    raising exceptions, and creating custom exceptions.
    """
    print("\n=== MANEJO DE EXCEPCIONES ===")

    # Bloque básico try/except
    print("\n-- Bloque básico try/except --")
    print("Intentando dividir por cero:")

    try:
        result = 10 / 0
        print(f"Resultado: {result}")  # Esta línea nunca se ejecuta
    except ZeroDivisionError:
        print("  Error: No se puede dividir por cero")

    # Manejando múltiples excepciones
    print("\n-- Manejando múltiples excepciones --")
    values = ["10", "20", "treinta", "40"]

    for val in values:
        try:
            num = int(val)
            result = 100 / num
            print(f"  100 / {val} = {result}")
        except ValueError:
            print(f"  Error: '{val}' no es un número válido")
        except ZeroDivisionError:
            print(f"  Error: No se puede dividir por {val} (cero)")

    # Cláusulas else y finally
    print("\n-- Cláusulas else y finally --")

    try:
        file_path = "archivo_temporal.txt"
        with open(file_path, "w") as f:
            f.write("Contenido de prueba")

        print(f"  Archivo '{file_path}' creado correctamente")
    except IOError as e:
        print(f"  Error de E/S: {e}")
    else:
        print("  El bloque 'else' se ejecuta cuando no hay excepciones")
        # Operaciones adicionales que solo se realizan si no hay errores
    finally:
        print("  El bloque 'finally' siempre se ejecuta")
        # Limpieza: eliminamos el archivo temporal
        try:
            os.remove(file_path)
            print(f"  Archivo '{file_path}' eliminado")
        except FileNotFoundError:
            pass

    # Capturando y analizando la excepción
    print("\n-- Capturando información de la excepción --")
    try:
        num = int("abc")
    except ValueError as e:
        print(f"  Error: {e}")
        print(f"  Tipo de excepción: {type(e).__name__}")
        print(f"  Argumentos: {e.args}")

    # Lanzando excepciones con raise
    print("\n-- Lanzando excepciones con raise --")

    def validate_age(age: int) -> None:
        """Validate that an age is within a reasonable range.

        Args:
            age: The age to validate

        Raises:
            ValueError: If age is negative or unreasonably high
        """
        if age < 0:
            raise ValueError("La edad no puede ser negativa")
        if age > 150:
            raise ValueError("La edad parece demasiado alta")
        print(f"  Edad {age} validada correctamente")

    try:
        validate_age(-5)
    except ValueError as e:
        print(f"  Validación fallida: {e}")

    try:
        validate_age(25)
    except ValueError as e:
        print(f"  Validación fallida: {e}")

    # Excepciones personalizadas
    print("\n-- Excepciones personalizadas --")

    class InsufficientFundsError(Exception):
        """Exception raised when there are insufficient funds for a withdrawal."""

        def __init__(self, balance: float, amount: float) -> None:
            self.balance = balance
            self.amount = amount
            self.deficit = amount - balance
            super().__init__(f"Saldo insuficiente: {balance}€. Intento de retirar: {amount}€. Faltan: {self.deficit}€")

    class BankAccount:
        """A simple bank account class to demonstrate custom exceptions."""

        def __init__(self, owner: str, balance: float = 0.0) -> None:
            self.owner = owner
            self.balance = balance

        def deposit(self, amount: float) -> None:
            """Add money to the account balance."""
            if amount <= 0:
                raise ValueError("El monto a depositar debe ser positivo")
            self.balance += amount
            print(f"  Depósito: {amount}€. Nuevo saldo: {self.balance}€")

        def withdraw(self, amount: float) -> None:
            """Withdraw money from the account.

            Args:
                amount: The amount to withdraw

            Raises:
                ValueError: If amount is negative
                InsufficientFundsError: If balance is less than amount
            """
            if amount <= 0:
                raise ValueError("El monto a retirar debe ser positivo")
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)

            self.balance -= amount
            print(f"  Retiro: {amount}€. Nuevo saldo: {self.balance}€")

    # Usar la clase con excepción personalizada
    account = BankAccount("Ana", 100.0)
    print(f"  Cuenta creada para {account.owner} con saldo inicial de {account.balance}€")

    try:
        account.deposit(50.0)
        account.withdraw(30.0)
        account.withdraw(200.0)  # Esto provocará la excepción
    except ValueError as e:
        print(f"  Error de valor: {e}")
    except InsufficientFundsError as e:
        print(f"  Error de fondos: {e}")
        print(f"  Déficit: {e.deficit}€")

    # Context Managers (with)
    print("\n-- Context Managers (with) --")

    class TempFile:
        """A context manager that creates a temporary file and deletes it afterwards."""

        def __init__(self, filename: str, mode: str = "w") -> None:
            self.filename = filename
            self.mode = mode
            self.file: Optional[TextIO] = None

        def __enter__(self) -> TextIO:
            """Called when entering the with block.

            Returns:
                The opened file object
            """
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
            """Called when exiting the with block.

            Args:
                exc_type: Exception type if an exception was raised
                exc_val: Exception value if an exception was raised
                exc_tb: Exception traceback if an exception was raised

            Returns:
                True if the exception was handled, False otherwise
            """
            if self.file:
                self.file.close()

            try:
                os.remove(self.filename)
                print(f"  Archivo temporal '{self.filename}' eliminado")
            except OSError:
                print(f"  No se pudo eliminar el archivo '{self.filename}'")

            return False  # Propagate exceptions

    # Uso del context manager personalizado
    try:
        with TempFile("archivo_temp.txt") as f:
            f.write("Este es un archivo temporal")
            print("  Contenido escrito en el archivo temporal")
            # Al salir del bloque with, el archivo se cerrará y eliminará automáticamente
    except Exception as e:
        print(f"  Error: {e}")

    # Try-except en una línea (Python 3.8+)
    print("\n-- Expresión try en una línea --")

    # Convertir a entero con valor por defecto si falla
    value = "123"
    num = int(value) if value.isdigit() else 0
    print(f"  Convertir '{value}' a entero: {num}")

    value = "abc"
    num = int(value) if value.isdigit() else 0
    print(f"  Convertir '{value}' a entero: {num}")

    # Ejercicio: Sistema de gestión de errores
    print("\n-- Ejercicio: Sistema de gestión de errores --")

    def divide_numbers(a: Union[int, float, str], b: Union[int, float, str]) -> float:
        """Divide two numbers with comprehensive error handling.

        Args:
            a: The numerator (can be number or string)
            b: The denominator (can be number or string)

        Returns:
            The result of a / b

        Raises:
            TypeError: If inputs cannot be converted to numbers
            ZeroDivisionError: If b is zero
            Exception: For any other error
        """
        try:
            # Intentar convertir a números si son strings
            num_a = float(a)
            num_b = float(b)

            # Comprobar división por cero
            if num_b == 0:
                raise ZeroDivisionError("No se puede dividir por cero")

            # Realizar la división
            result = num_a / num_b
            return result

        except ValueError:
            # Error de conversión
            raise TypeError(f"No se pueden convertir los valores a números: '{a}', '{b}'")
        except ZeroDivisionError as e:
            # Re-lanzar con el mismo mensaje
            raise e
        except Exception as e:
            # Capturar cualquier otra excepción
            raise Exception(f"Error inesperado: {e}")

    # Probar la función con diferentes casos
    test_cases = [
        (10, 2),        # Normal: 5.0
        ("8", "4"),     # Strings convertibles: 2.0
        (5, 0),         # División por cero
        ("cinco", 2),   # String no convertible
    ]

    for a, b in test_cases:
        try:
            result = divide_numbers(a, b)
            print(f"  {a} / {b} = {result}")
        except Exception as e:
            print(f"  Error al dividir {a} / {b}: {e}")


# Funciones exportables para ser utilizadas por otros módulos
def safe_operation(operation: Callable[..., Any], *args: Any, default: Any = None, **kwargs: Any) -> Any:
    """Safely execute an operation, returning a default value if it fails.

    Args:
        operation: The function to execute
        *args: Arguments to pass to the operation
        default: Value to return if the operation fails
        **kwargs: Keyword arguments to pass to the operation

    Returns:
        The result of the operation or the default value if it fails
    """
    try:
        return operation(*args, **kwargs)
    except Exception as e:
        return default


def retry(max_attempts: int = 3, delay: float = 1.0):
    """Decorator that retries a function if it raises an exception.

    Args:
        max_attempts: Maximum number of attempts
        delay: Delay between attempts in seconds

    Returns:
        The decorated function
    """
    import time
    from functools import wraps

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    print(f"Intento {attempts} fallido: {e}. Reintentando en {delay} segundos...")
                    time.sleep(delay)
            return None  # This line should never be reached
        return wrapper
    return decorator


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    exception_handling()

    # Demostración de las funciones exportables
    print("\n-- Demostración de funciones exportables --")

    # Ejemplo de safe_operation
    result = safe_operation(int, "123", default=0)
    print(f"safe_operation(int, '123', default=0): {result}")

    result = safe_operation(int, "abc", default=0)
    print(f"safe_operation(int, 'abc', default=0): {result}")

    # Ejemplo de retry
    @retry(max_attempts=2, delay=0.1)
    def unstable_function(succeed_on_attempt: int, current_attempt: List[int] = None) -> str:
        if current_attempt is None:
            current_attempt = [0]

        current_attempt[0] += 1
        if current_attempt[0] < succeed_on_attempt:
            raise ValueError(f"Fallo simulado en el intento {current_attempt[0]}")
        return "Operación exitosa"

    try:
        # Debería tener éxito en el segundo intento
        result = unstable_function(2)
        print(f"unstable_function(2): {result}")

        # Debería fallar después de 2 intentos
        result = unstable_function(3)
        print(f"unstable_function(3): {result}")
    except Exception as e:
        print(f"Error final: {e}")
