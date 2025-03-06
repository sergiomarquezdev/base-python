"""
Advanced Data Types in Python

This module demonstrates advanced data types in Python,
including lists, tuples, sets, dictionaries, and related operations.
"""

from typing import Any, Dict, List, Tuple, Set, Callable
from functools import reduce


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

    # reduce (functools)
    product = reduce(lambda x, y: x * y, numbers)
    print(f"reduce (producto): {product}")

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


# Funciones útiles para exportar
def merge_dictionaries(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge two dictionaries into a new one.

    Args:
        dict1: The first dictionary
        dict2: The second dictionary

    Returns:
        A new dictionary containing all key-value pairs from both inputs
    """
    return {**dict1, **dict2}


def filter_list(items: List[Any], predicate: Callable[[Any], bool]) -> List[Any]:
    """Filter a list using a predicate function.

    Args:
        items: The list of items to filter
        predicate: A function that returns True for items to keep

    Returns:
        A new list containing only the items for which predicate returns True
    """
    return [item for item in items if predicate(item)]


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    advanced_types()

    # Demostración de las funciones exportables
    print("\n-- Demostración de funciones exportables --")
    dict_result = merge_dictionaries({"a": 1}, {"b": 2})
    print(f"merge_dictionaries(): {dict_result}")

    filtered = filter_list([1, 2, 3, 4, 5], lambda x: x > 2)
    print(f"filter_list(): {filtered}")
