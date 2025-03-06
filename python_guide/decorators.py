"""
Decorators in Python

This module demonstrates decorators in Python,
including basic decorators, decorators with arguments,
and practical examples of their use.
"""

import time
import functools
from typing import Any, Callable, Dict, List, Optional, TypeVar, cast
from functools import wraps


# Type variables for better type hinting with decorators
F = TypeVar('F', bound=Callable[..., Any])


def decorators_examples() -> None:
    """Demonstrate decorators in Python.

    Covers basic decorators, decorators with arguments,
    class decorators, and practical examples.
    """
    print("\n=== DECORADORES ===")

    # Funciones como objetos de primera clase
    print("\n-- Funciones como objetos de primera clase --")

    def greet(name: str) -> str:
        """Return a greeting message."""
        return f"¡Hola, {name}!"

    # Asignar una función a una variable
    greeting_function = greet
    print(f"Llamada a través de variable: {greeting_function('Ana')}")

    # Pasar una función como argumento
    def execute_function(func: Callable[[str], str], arg: str) -> str:
        """Execute a function with the given argument."""
        return func(arg)

    print(f"Pasando función como argumento: {execute_function(greet, 'Carlos')}")

    # Retornar una función desde otra función
    def get_greeting_function() -> Callable[[str], str]:
        """Return a greeting function."""
        return greet

    returned_function = get_greeting_function()
    print(f"Función retornada: {returned_function('Laura')}")

    # Closures
    print("\n-- Closures --")

    def make_multiplier(factor: float) -> Callable[[float], float]:
        """Create a function that multiplies its argument by factor.

        Args:
            factor: The multiplication factor

        Returns:
            A function that multiplies its input by factor
        """
        # La función interna tiene acceso a la variable 'factor'
        # del ámbito externo, incluso después de que make_multiplier haya terminado
        def multiplier(x: float) -> float:
            return x * factor

        return multiplier

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")

    # Decoradores básicos
    print("\n-- Decoradores básicos --")

    def simple_decorator(func: F) -> F:
        """A simple decorator that prints messages before and after function execution.

        Args:
            func: The function to decorate

        Returns:
            The decorated function
        """
        @wraps(func)  # Preserva metadatos de la función original
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"Antes de llamar a {func.__name__}")
            result = func(*args, **kwargs)
            print(f"Después de llamar a {func.__name__}")
            return result

        return cast(F, wrapper)

    # Aplicar el decorador con la sintaxis @
    @simple_decorator
    def say_hello(name: str) -> str:
        """Say hello to someone."""
        return f"¡Hola, {name}!"

    # Equivalente a: say_hello = simple_decorator(say_hello)

    print(f"Llamando a función decorada: {say_hello('Miguel')}")
    print(f"Nombre de la función: {say_hello.__name__}")
    print(f"Docstring: {say_hello.__doc__}")

    # Decoradores con argumentos
    print("\n-- Decoradores con argumentos --")

    def repeat(times: int) -> Callable[[F], F]:
        """A decorator that repeats the function call a specified number of times.

        Args:
            times: Number of times to repeat the function call

        Returns:
            A decorator function
        """
        def decorator(func: F) -> F:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                result = None
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return cast(F, wrapper)
        return decorator

    @repeat(times=3)
    def say_hi() -> None:
        """Say hi."""
        print("¡Hola!")

    print("Llamando a función decorada con argumentos:")
    say_hi()

    # Múltiples decoradores
    print("\n-- Múltiples decoradores --")

    def bold(func: F) -> F:
        """Make the output text bold with HTML tags."""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return f"<b>{func(*args, **kwargs)}</b>"
        return cast(F, wrapper)

    def italic(func: F) -> F:
        """Make the output text italic with HTML tags."""
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return f"<i>{func(*args, **kwargs)}</i>"
        return cast(F, wrapper)

    @bold
    @italic
    def format_text(text: str) -> str:
        """Format the given text."""
        return text

    # Equivalente a: format_text = bold(italic(format_text))
    # Se aplican de abajo hacia arriba

    print(f"Texto con múltiples decoradores: {format_text('Texto formateado')}")

    # Decoradores de clase
    print("\n-- Decoradores de clase --")

    def add_greeting(cls: type) -> type:
        """Add a greeting method to a class.

        Args:
            cls: The class to decorate

        Returns:
            The decorated class
        """
        def greet(self, name: str) -> str:
            return f"¡Hola, {name}! Soy {self.__class__.__name__}"

        cls.greet = greet  # type: ignore
        return cls

    @add_greeting
    class Person:
        """A simple person class."""

        def __init__(self, name: str) -> None:
            self.name = name

    person = Person("Juan")
    print(f"Método añadido por decorador: {person.greet('Ana')}")  # type: ignore

    # Ejemplos prácticos
    print("\n-- Ejemplos prácticos --")

    # 1. Medir tiempo de ejecución
    def timing_decorator(func: F) -> F:
        """Measure and print the execution time of a function.

        Args:
            func: The function to time

        Returns:
            The decorated function
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Función {func.__name__} tomó {end_time - start_time:.6f} segundos")
            return result
        return cast(F, wrapper)

    @timing_decorator
    def slow_function() -> None:
        """A function that takes some time to execute."""
        time.sleep(0.5)

    print("Ejecutando función con decorador de tiempo:")
    slow_function()

    # 2. Caché de resultados
    def memoize(func: F) -> F:
        """Cache the results of a function call.

        Args:
            func: The function to cache

        Returns:
            The decorated function with caching
        """
        cache: Dict[Any, Any] = {}

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Crear una clave para el caché basada en los argumentos
            key = str(args) + str(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
                print(f"Calculando resultado para {key}")
            else:
                print(f"Usando resultado en caché para {key}")
            return cache[key]

        return cast(F, wrapper)

    @memoize
    def fibonacci(n: int) -> int:
        """Calculate the nth Fibonacci number recursively."""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("\nCalculando Fibonacci con memoización:")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) de nuevo = {fibonacci(10)}")  # Debería usar el caché

    # 3. Validación de argumentos
    def validate_args(*types: type) -> Callable[[F], F]:
        """Validate that function arguments match the specified types.

        Args:
            *types: The expected types for each argument

        Returns:
            A decorator function
        """
        def decorator(func: F) -> F:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                if len(args) != len(types):
                    raise ValueError(
                        f"Se esperaban {len(types)} argumentos, pero se recibieron {len(args)}"
                    )

                for i, (arg, expected_type) in enumerate(zip(args, types)):
                    if not isinstance(arg, expected_type):
                        raise TypeError(
                            f"Argumento {i+1} debe ser {expected_type.__name__}, "
                            f"pero es {type(arg).__name__}"
                        )

                return func(*args, **kwargs)
            return cast(F, wrapper)
        return decorator

    @validate_args(str, int)
    def greet_n_times(name: str, times: int) -> str:
        """Greet someone a specified number of times.

        Args:
            name: The name to greet
            times: Number of times to repeat the greeting

        Returns:
            The greeting message repeated
        """
        return f"¡Hola, {name}! " * times

    print("\nValidación de argumentos:")
    try:
        print(greet_n_times("Pedro", 3))
        print(greet_n_times(123, 3))  # Esto debería fallar
    except TypeError as e:
        print(f"Error de tipo: {e}")

    # 4. Registro (logging)
    def log_calls(func: F) -> F:
        """Log function calls with their arguments and return values.

        Args:
            func: The function to log

        Returns:
            The decorated function
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Llamando a {func.__name__}({signature})")
            result = func(*args, **kwargs)
            print(f"{func.__name__} retornó {result!r}")

            return result
        return cast(F, wrapper)

    @log_calls
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    print("\nRegistro de llamadas:")
    add(3, 5)

    # 5. Control de acceso
    def require_auth(func: F) -> F:
        """Simulate requiring authentication for a function.

        Args:
            func: The function to protect

        Returns:
            The decorated function
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Simulación simple de autenticación
            is_authenticated = kwargs.pop('is_authenticated', False)

            if is_authenticated:
                return func(*args, **kwargs)
            else:
                return "Acceso denegado: autenticación requerida"

        return cast(F, wrapper)

    @require_auth
    def get_sensitive_data() -> str:
        """Return some sensitive data."""
        return "Datos confidenciales: 1234567890"

    print("\nControl de acceso:")
    print(f"Sin autenticación: {get_sensitive_data()}")
    print(f"Con autenticación: {get_sensitive_data(is_authenticated=True)}")

    # Ejercicio: Crear un decorador personalizado
    print("\n-- Ejercicio: Crear un decorador personalizado --")

    def retry(max_attempts: int = 3, delay: float = 1.0) -> Callable[[F], F]:
        """Retry a function if it raises an exception.

        Args:
            max_attempts: Maximum number of attempts
            delay: Delay between attempts in seconds

        Returns:
            The decorated function
        """
        def decorator(func: F) -> F:
            @wraps(func)
            def wrapper(*args: Any, **kwargs: Any) -> Any:
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
            return cast(F, wrapper)
        return decorator

    @retry(max_attempts=3, delay=0.1)
    def unstable_function(succeed_on_attempt: int, current_attempt: List[int] = None) -> str:
        """A function that fails until a specific attempt.

        Args:
            succeed_on_attempt: The attempt number on which to succeed
            current_attempt: A mutable list to track the current attempt

        Returns:
            A success message

        Raises:
            ValueError: If the current attempt is less than succeed_on_attempt
        """
        if current_attempt is None:
            current_attempt = [0]

        current_attempt[0] += 1
        if current_attempt[0] < succeed_on_attempt:
            raise ValueError(f"Fallo simulado en el intento {current_attempt[0]}")
        return "Operación exitosa"

    try:
        # Debería tener éxito en el segundo intento
        result = unstable_function(2)
        print(f"Resultado: {result}")

        # Debería fallar después de 3 intentos
        result = unstable_function(5)
        print(f"Resultado: {result}")
    except ValueError as e:
        print(f"Error final: {e}")


# Decoradores exportables para ser utilizados por otros módulos
def debug(func: F) -> F:
    """Print debug information about a function call.

    Args:
        func: The function to debug

    Returns:
        The decorated function
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"DEBUG: Llamando a {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"DEBUG: {func.__name__} retornó {result!r}")

        return result

    return cast(F, wrapper)


def timer(func: F) -> F:
    """Measure and print the execution time of a function.

    Args:
        func: The function to time

    Returns:
        The decorated function
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")
        return result

    return cast(F, wrapper)


def deprecated(message: str = "") -> Callable[[F], F]:
    """Mark a function as deprecated and print a warning when it's called.

    Args:
        message: Optional message explaining why the function is deprecated

    Returns:
        A decorator function
    """
    def decorator(func: F) -> F:
        warning = message or f"La función {func.__name__} está obsoleta y será eliminada en futuras versiones."

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print(f"ADVERTENCIA: {warning}")
            return func(*args, **kwargs)

        return cast(F, wrapper)

    return decorator


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    decorators_examples()

    # Demostración de los decoradores exportables
    print("\n-- Demostración de decoradores exportables --")

    @debug
    def add_numbers(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    print("\nUsando el decorador debug:")
    add_numbers(5, 7)

    @timer
    def slow_operation() -> None:
        """A slow operation."""
        time.sleep(0.2)

    print("\nUsando el decorador timer:")
    slow_operation()

    @deprecated("Use la función 'add_numbers' en su lugar.")
    def sum_numbers(a: int, b: int) -> int:
        """Add two numbers (deprecated)."""
        return a + b

    print("\nUsando el decorador deprecated:")
    sum_numbers(10, 20)
