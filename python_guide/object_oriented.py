"""
Object-Oriented Programming in Python

This module demonstrates object-oriented programming concepts in Python,
including classes, inheritance, encapsulation, and polymorphism.
"""

from typing import Any, Dict, List, Optional, Union, Tuple
from abc import ABC, abstractmethod
from dataclasses import dataclass
import math


def object_oriented() -> None:
    """Demonstrate object-oriented programming concepts in Python.

    Covers classes, objects, inheritance, encapsulation, polymorphism,
    special methods, properties, and more.
    """
    print("\n=== PROGRAMACIÓN ORIENTADA A OBJETOS ===")

    # Clases y objetos básicos
    print("\n-- Clases y objetos básicos --")

    class Person:
        """A simple class representing a person."""

        def __init__(self, name: str, age: int) -> None:
            """Initialize a new Person instance.

            Args:
                name: The person's name
                age: The person's age
            """
            self.name = name
            self.age = age

        def greet(self) -> str:
            """Return a greeting message.

            Returns:
                A greeting string
            """
            return f"Hola, me llamo {self.name} y tengo {self.age} años."

        def have_birthday(self) -> None:
            """Increment the person's age by 1."""
            self.age += 1
            print(f"¡Feliz cumpleaños! Ahora {self.name} tiene {self.age} años.")

    # Crear instancias de la clase
    person1 = Person("Ana", 30)
    person2 = Person("Carlos", 25)

    print(f"Persona 1: {person1.name}, {person1.age} años")
    print(f"Persona 2: {person2.name}, {person2.age} años")

    print(f"Saludo de persona 1: {person1.greet()}")
    person1.have_birthday()

    # Herencia
    print("\n-- Herencia --")

    class Student(Person):
        """A class representing a student, inheriting from Person."""

        def __init__(self, name: str, age: int, student_id: str, major: str) -> None:
            """Initialize a new Student instance.

            Args:
                name: The student's name
                age: The student's age
                student_id: The student's ID
                major: The student's major
            """
            # Llamar al constructor de la clase padre
            super().__init__(name, age)
            self.student_id = student_id
            self.major = major

        def greet(self) -> str:
            """Override the greet method to include student information.

            Returns:
                A greeting string with student details
            """
            # Extender el método de la clase padre
            basic_greeting = super().greet()
            return f"{basic_greeting} Soy estudiante de {self.major} (ID: {self.student_id})."

        def study(self, subject: str) -> None:
            """Simulate studying a subject.

            Args:
                subject: The subject being studied
            """
            print(f"{self.name} está estudiando {subject}.")

    # Crear una instancia de la clase derivada
    student = Student("Laura", 22, "S12345", "Informática")

    print(f"Estudiante: {student.name}, {student.age} años, ID: {student.student_id}, Carrera: {student.major}")
    print(f"Saludo de estudiante: {student.greet()}")
    student.study("Programación Python")

    # Verificar relaciones de herencia
    print(f"¿student es instancia de Student? {isinstance(student, Student)}")
    print(f"¿student es instancia de Person? {isinstance(student, Person)}")
    print(f"¿Student es subclase de Person? {issubclass(Student, Person)}")

    # Encapsulación
    print("\n-- Encapsulación --")

    class BankAccount:
        """A class demonstrating encapsulation with private attributes."""

        def __init__(self, owner: str, balance: float = 0.0) -> None:
            self.owner = owner
            self._balance = balance  # Atributo "protegido" (convención)
            self.__secret_pin = "1234"  # Atributo "privado" (name mangling)

        def deposit(self, amount: float) -> None:
            """Add money to the account."""
            if amount <= 0:
                raise ValueError("El monto debe ser positivo")
            self._balance += amount
            print(f"Depósito: {amount}€. Nuevo saldo: {self._balance}€")

        def withdraw(self, amount: float) -> None:
            """Withdraw money from the account."""
            if amount <= 0:
                raise ValueError("El monto debe ser positivo")
            if amount > self._balance:
                raise ValueError("Fondos insuficientes")
            self._balance -= amount
            print(f"Retiro: {amount}€. Nuevo saldo: {self._balance}€")

        def get_balance(self) -> float:
            """Get the current balance."""
            return self._balance

        def _internal_operation(self) -> None:
            """An internal method (protected by convention)."""
            print("Esta es una operación interna.")

        def __very_private_method(self) -> None:
            """A private method (name mangling)."""
            print("Este método es muy privado.")

        def access_private(self) -> None:
            """Access private method to demonstrate it works."""
            self.__very_private_method()
            print(f"PIN secreto: {self.__secret_pin}")

    account = BankAccount("Juan", 1000.0)
    print(f"Cuenta de {account.owner}, saldo: {account.get_balance()}€")

    account.deposit(500)
    account.withdraw(200)

    # Acceso a atributos protegidos (posible, pero no recomendado)
    print(f"Acceso directo a _balance (no recomendado): {account._balance}€")

    # Intentar acceder a atributos privados
    try:
        print(account.__secret_pin)  # Esto fallará
    except AttributeError as e:
        print(f"Error al acceder a __secret_pin: {e}")

    # Pero el name mangling permite acceder si conoces el patrón
    print(f"Acceso con name mangling: {account._BankAccount__secret_pin}")

    # Acceder a métodos privados a través de métodos públicos
    account.access_private()

    # Propiedades (@property)
    print("\n-- Propiedades (@property) --")

    class Temperature:
        """A class demonstrating properties for controlled attribute access."""

        def __init__(self, celsius: float = 0.0) -> None:
            self._celsius = celsius

        @property
        def celsius(self) -> float:
            """Get the temperature in Celsius."""
            return self._celsius

        @celsius.setter
        def celsius(self, value: float) -> None:
            """Set the temperature in Celsius."""
            if value < -273.15:
                raise ValueError("La temperatura no puede ser menor que el cero absoluto")
            self._celsius = value

        @property
        def fahrenheit(self) -> float:
            """Get the temperature in Fahrenheit."""
            return (self._celsius * 9/5) + 32

        @fahrenheit.setter
        def fahrenheit(self, value: float) -> None:
            """Set the temperature in Fahrenheit."""
            celsius = (value - 32) * 5/9
            if celsius < -273.15:
                raise ValueError("La temperatura no puede ser menor que el cero absoluto")
            self._celsius = celsius

        @property
        def kelvin(self) -> float:
            """Get the temperature in Kelvin."""
            return self._celsius + 273.15

        @kelvin.setter
        def kelvin(self, value: float) -> None:
            """Set the temperature in Kelvin."""
            if value < 0:
                raise ValueError("La temperatura en Kelvin no puede ser negativa")
            self._celsius = value - 273.15

    temp = Temperature(25)
    print(f"Temperatura en Celsius: {temp.celsius}°C")
    print(f"Temperatura en Fahrenheit: {temp.fahrenheit}°F")
    print(f"Temperatura en Kelvin: {temp.kelvin}K")

    temp.fahrenheit = 68
    print(f"Después de cambiar a 68°F: {temp.celsius}°C")

    temp.kelvin = 300
    print(f"Después de cambiar a 300K: {temp.celsius}°C")

    try:
        temp.celsius = -300  # Esto debería fallar
    except ValueError as e:
        print(f"Error al establecer temperatura: {e}")

    # Métodos especiales (dunder methods)
    print("\n-- Métodos especiales (dunder methods) --")

    class Vector2D:
        """A class representing a 2D vector with special methods."""

        def __init__(self, x: float = 0, y: float = 0) -> None:
            self.x = x
            self.y = y

        def __str__(self) -> str:
            """String representation for end users."""
            return f"Vector2D({self.x}, {self.y})"

        def __repr__(self) -> str:
            """String representation for developers."""
            return f"Vector2D(x={self.x}, y={self.y})"

        def __add__(self, other: 'Vector2D') -> 'Vector2D':
            """Add two vectors."""
            return Vector2D(self.x + other.x, self.y + other.y)

        def __sub__(self, other: 'Vector2D') -> 'Vector2D':
            """Subtract two vectors."""
            return Vector2D(self.x - other.x, self.y - other.y)

        def __mul__(self, scalar: float) -> 'Vector2D':
            """Multiply vector by scalar."""
            return Vector2D(self.x * scalar, self.y * scalar)

        def __eq__(self, other: object) -> bool:
            """Check if two vectors are equal."""
            if not isinstance(other, Vector2D):
                return False
            return self.x == other.x and self.y == other.y

        def __abs__(self) -> float:
            """Get the magnitude (length) of the vector."""
            return math.sqrt(self.x**2 + self.y**2)

        def __bool__(self) -> bool:
            """Check if the vector is non-zero."""
            return self.x != 0 or self.y != 0

        def __getitem__(self, index: int) -> float:
            """Access vector components by index."""
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError("Vector2D solo tiene 2 componentes")

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1: {v1}")
    print(f"Representación para desarrolladores: {repr(v1)}")

    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")

    v4 = v1 - v2
    print(f"v1 - v2 = {v4}")

    v5 = v1 * 2
    print(f"v1 * 2 = {v5}")

    print(f"¿v1 == v2? {v1 == v2}")
    print(f"¿v1 == Vector2D(3, 4)? {v1 == Vector2D(3, 4)}")

    print(f"Magnitud de v1: {abs(v1)}")
    print(f"¿v1 es no-cero? {bool(v1)}")

    print(f"v1[0] = {v1[0]}, v1[1] = {v1[1]}")

    try:
        print(v1[2])
    except IndexError as e:
        print(f"Error de índice: {e}")

    # Métodos de clase y estáticos
    print("\n-- Métodos de clase y estáticos --")

    class MathUtils:
        """A class demonstrating class and static methods."""

        # Variable de clase
        PI = 3.14159

        def __init__(self) -> None:
            # No necesitamos inicializar nada
            pass

        @staticmethod
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

        @classmethod
        def circle_area(cls, radius: float) -> float:
            """Calculate the area of a circle.

            Args:
                radius: The radius of the circle

            Returns:
                The area of the circle
            """
            return cls.PI * radius * radius

        @classmethod
        def update_pi(cls, new_pi: float) -> None:
            """Update the PI constant.

            Args:
                new_pi: The new value for PI
            """
            cls.PI = new_pi

    # Usar métodos estáticos
    print(f"¿17 es primo? {MathUtils.is_prime(17)}")
    print(f"¿20 es primo? {MathUtils.is_prime(20)}")

    # Usar métodos de clase
    print(f"Área de un círculo con radio 5: {MathUtils.circle_area(5)}")

    # Cambiar la variable de clase
    print(f"PI original: {MathUtils.PI}")
    MathUtils.update_pi(3.14159265359)
    print(f"PI actualizado: {MathUtils.PI}")
    print(f"Área recalculada: {MathUtils.circle_area(5)}")

    # Polimorfismo
    print("\n-- Polimorfismo --")

    class Shape(ABC):
        """Abstract base class for shapes."""

        @abstractmethod
        def area(self) -> float:
            """Calculate the area of the shape."""
            pass

        @abstractmethod
        def perimeter(self) -> float:
            """Calculate the perimeter of the shape."""
            pass

        def describe(self) -> str:
            """Describe the shape."""
            return f"Soy una forma con área {self.area()} y perímetro {self.perimeter()}"

    class Circle(Shape):
        """A circle shape."""

        def __init__(self, radius: float) -> None:
            self.radius = radius

        def area(self) -> float:
            """Calculate the area of the circle."""
            return math.pi * self.radius * self.radius

        def perimeter(self) -> float:
            """Calculate the perimeter (circumference) of the circle."""
            return 2 * math.pi * self.radius

        def describe(self) -> str:
            """Override the describe method."""
            return f"Soy un círculo con radio {self.radius}"

    class Rectangle(Shape):
        """A rectangle shape."""

        def __init__(self, width: float, height: float) -> None:
            self.width = width
            self.height = height

        def area(self) -> float:
            """Calculate the area of the rectangle."""
            return self.width * self.height

        def perimeter(self) -> float:
            """Calculate the perimeter of the rectangle."""
            return 2 * (self.width + self.height)

        def describe(self) -> str:
            """Override the describe method."""
            return f"Soy un rectángulo de {self.width}x{self.height}"

    # No podemos instanciar una clase abstracta
    try:
        shape = Shape()
    except TypeError as e:
        print(f"Error al instanciar Shape: {e}")

    # Crear instancias de las clases concretas
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    # Lista de formas (polimorfismo)
    shapes: List[Shape] = [circle, rectangle]

    # Iterar sobre las formas y llamar a sus métodos
    for i, shape in enumerate(shapes, 1):
        print(f"Forma {i}: {shape.describe()}")
        print(f"  Área: {shape.area()}")
        print(f"  Perímetro: {shape.perimeter()}")

    # Dataclasses (Python 3.7+)
    print("\n-- Dataclasses --")

    @dataclass
    class Point:
        """A simple dataclass representing a point in 2D space."""
        x: float
        y: float

        def distance_from_origin(self) -> float:
            """Calculate the distance from the origin."""
            return math.sqrt(self.x**2 + self.y**2)

    @dataclass
    class ColorPoint(Point):
        """A point with a color."""
        color: str = "black"

    p1 = Point(3, 4)
    p2 = Point(3, 4)
    p3 = ColorPoint(5, 12, "red")

    print(f"p1: {p1}")
    print(f"¿p1 == p2? {p1 == p2}")  # Comparación automática
    print(f"p3: {p3}")
    print(f"Distancia de p1 al origen: {p1.distance_from_origin()}")
    print(f"Distancia de p3 al origen: {p3.distance_from_origin()}")

    # Ejercicio: Sistema de gestión de biblioteca
    print("\n-- Ejercicio: Sistema de gestión de biblioteca --")

    class LibraryItem(ABC):
        """Abstract base class for library items."""

        def __init__(self, title: str, item_id: str) -> None:
            self.title = title
            self.item_id = item_id
            self.checked_out = False

        @abstractmethod
        def display_info(self) -> str:
            """Display information about the item."""
            pass

        def check_out(self) -> None:
            """Check out the item."""
            if self.checked_out:
                raise ValueError(f"El ítem '{self.title}' ya está prestado")
            self.checked_out = True
            print(f"'{self.title}' ha sido prestado")

        def return_item(self) -> None:
            """Return the item."""
            if not self.checked_out:
                raise ValueError(f"El ítem '{self.title}' no está prestado")
            self.checked_out = False
            print(f"'{self.title}' ha sido devuelto")

    class Book(LibraryItem):
        """A book in the library."""

        def __init__(self, title: str, item_id: str, author: str, pages: int) -> None:
            super().__init__(title, item_id)
            self.author = author
            self.pages = pages

        def display_info(self) -> str:
            """Display information about the book."""
            status = "prestado" if self.checked_out else "disponible"
            return f"Libro: '{self.title}' por {self.author}, {self.pages} páginas, {status}"

    class DVD(LibraryItem):
        """A DVD in the library."""

        def __init__(self, title: str, item_id: str, director: str, runtime: int) -> None:
            super().__init__(title, item_id)
            self.director = director
            self.runtime = runtime

        def display_info(self) -> str:
            """Display information about the DVD."""
            status = "prestado" if self.checked_out else "disponible"
            return f"DVD: '{self.title}' dirigido por {self.director}, {self.runtime} minutos, {status}"

    class Library:
        """A library that manages items."""

        def __init__(self, name: str) -> None:
            self.name = name
            self.items: Dict[str, LibraryItem] = {}

        def add_item(self, item: LibraryItem) -> None:
            """Add an item to the library."""
            if item.item_id in self.items:
                raise ValueError(f"Ya existe un ítem con ID {item.item_id}")
            self.items[item.item_id] = item
            print(f"Ítem '{item.title}' añadido a la biblioteca")

        def check_out_item(self, item_id: str) -> None:
            """Check out an item from the library."""
            if item_id not in self.items:
                raise ValueError(f"No existe un ítem con ID {item_id}")
            self.items[item_id].check_out()

        def return_item(self, item_id: str) -> None:
            """Return an item to the library."""
            if item_id not in self.items:
                raise ValueError(f"No existe un ítem con ID {item_id}")
            self.items[item_id].return_item()

        def display_available_items(self) -> None:
            """Display all available items."""
            print(f"Ítems disponibles en {self.name}:")
            available = [item for item in self.items.values() if not item.checked_out]
            if not available:
                print("  No hay ítems disponibles")
            else:
                for i, item in enumerate(available, 1):
                    print(f"  {i}. {item.display_info()}")

        def display_all_items(self) -> None:
            """Display all items."""
            print(f"Todos los ítems en {self.name}:")
            if not self.items:
                print("  No hay ítems en la biblioteca")
            else:
                for i, item in enumerate(self.items.values(), 1):
                    print(f"  {i}. {item.display_info()}")

    # Crear una biblioteca y añadir ítems
    library = Library("Biblioteca Central")

    book1 = Book("El Quijote", "B001", "Miguel de Cervantes", 863)
    book2 = Book("Cien años de soledad", "B002", "Gabriel García Márquez", 417)
    dvd1 = DVD("El Padrino", "D001", "Francis Ford Coppola", 175)

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(dvd1)

    # Mostrar todos los ítems
    library.display_all_items()

    # Prestar y devolver ítems
    library.check_out_item("B001")
    library.display_available_items()

    library.return_item("B001")
    library.display_available_items()


# Clases exportables para ser utilizadas por otros módulos
class Rectangle:
    """A rectangle with width and height."""

    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with the given width and height.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle.

        Returns:
            The area (width * height)
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle.

        Returns:
            The perimeter (2 * (width + height))
        """
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """String representation of the rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle:
    """A circle with a radius."""

    def __init__(self, radius: float) -> None:
        """Initialize a circle with the given radius.

        Args:
            radius: The radius of the circle
        """
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle.

        Returns:
            The area (π * radius²)
        """
        return math.pi * self.radius * self.radius

    def circumference(self) -> float:
        """Calculate the circumference of the circle.

        Returns:
            The circumference (2 * π * radius)
        """
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        """String representation of the circle."""
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    object_oriented()

    # Demostración de las clases exportables
    print("\n-- Demostración de clases exportables --")

    rect = Rectangle(5, 10)
    print(f"Rectángulo: {rect}")
    print(f"Área: {rect.area()}")
    print(f"Perímetro: {rect.perimeter()}")

    circle = Circle(7)
    print(f"Círculo: {circle}")
    print(f"Área: {circle.area()}")
    print(f"Circunferencia: {circle.circumference()}")
