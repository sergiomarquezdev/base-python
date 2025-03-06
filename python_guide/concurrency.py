"""
Concurrency and Parallelism in Python

This module demonstrates concurrency and parallelism in Python,
including threading, multiprocessing, and asynchronous programming.
"""

import time
import threading
import multiprocessing
import asyncio
import concurrent.futures
import requests
import random
import os
from typing import Any, List, Dict, Callable, Optional, Union, Tuple, Set


def concurrency_examples() -> None:
    """Demonstrate concurrency and parallelism concepts in Python.

    Covers threading, multiprocessing, asyncio, and concurrent.futures.
    """
    print("\n=== CONCURRENCIA Y PARALELISMO ===")

    # Introducción a la concurrencia vs paralelismo
    print("\n-- Introducción a la concurrencia vs paralelismo --")
    print("Concurrencia: Gestionar múltiples tareas al mismo tiempo (no necesariamente ejecutándolas simultáneamente).")
    print("Paralelismo: Ejecutar múltiples tareas simultáneamente (requiere múltiples núcleos/procesadores).")
    print("Python ofrece varias opciones para concurrencia y paralelismo:")
    print("  - threading: Para tareas limitadas por I/O")
    print("  - multiprocessing: Para tareas limitadas por CPU")
    print("  - asyncio: Para programación asíncrona basada en eventos")
    print("  - concurrent.futures: API de alto nivel para threading y multiprocessing")

    # Ejecución secuencial (para comparación)
    print("\n-- Ejecución secuencial --")

    def io_bound_task(task_id: int, delay: float) -> Tuple[int, float]:
        """Simulate an I/O-bound task with a delay.

        Args:
            task_id: The task identifier
            delay: The delay in seconds

        Returns:
            A tuple of (task_id, execution_time)
        """
        start_time = time.time()
        print(f"Tarea {task_id} iniciada")
        time.sleep(delay)  # Simular operación de I/O
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tarea {task_id} completada en {execution_time:.2f} segundos")
        return task_id, execution_time

    def cpu_bound_task(task_id: int, iterations: int) -> Tuple[int, float]:
        """Simulate a CPU-bound task with iterations.

        Args:
            task_id: The task identifier
            iterations: The number of iterations

        Returns:
            A tuple of (task_id, execution_time)
        """
        start_time = time.time()
        print(f"Tarea CPU {task_id} iniciada")

        # Operación intensiva en CPU
        result = 0
        for i in range(iterations):
            result += i * i

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tarea CPU {task_id} completada en {execution_time:.2f} segundos")
        return task_id, execution_time

    print("Ejecutando tareas secuencialmente:")
    sequential_start = time.time()

    # Ejecutar 3 tareas I/O-bound secuencialmente
    results = []
    for i in range(3):
        results.append(io_bound_task(i, 0.5))

    sequential_end = time.time()
    print(f"Tiempo total secuencial: {sequential_end - sequential_start:.2f} segundos")

    # Threading (para tareas I/O-bound)
    print("\n-- Threading (para tareas I/O-bound) --")

    def threaded_io_tasks() -> None:
        """Run I/O-bound tasks using threads."""
        threads = []
        results = []

        # Crear y iniciar hilos
        for i in range(3):
            thread = threading.Thread(target=lambda i=i: results.append(io_bound_task(i, 0.5)))
            threads.append(thread)
            thread.start()

        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()

    print("Ejecutando tareas con threading:")
    threaded_start = time.time()
    threaded_io_tasks()
    threaded_end = time.time()
    print(f"Tiempo total con threading: {threaded_end - threaded_start:.2f} segundos")

    # Compartir datos entre hilos
    print("\n-- Compartir datos entre hilos --")

    # Usar un Lock para evitar condiciones de carrera
    counter = 0
    counter_lock = threading.Lock()

    def increment_counter(amount: int, repetitions: int) -> None:
        """Increment a shared counter with lock protection.

        Args:
            amount: The amount to increment by
            repetitions: The number of times to increment
        """
        global counter
        for _ in range(repetitions):
            with counter_lock:  # Adquirir el lock
                counter += amount
                # El lock se libera automáticamente al salir del bloque with

    # Crear y ejecutar hilos que modifican el contador
    threads = []
    for i in range(5):
        thread = threading.Thread(target=increment_counter, args=(i+1, 100000))
        threads.append(thread)
        thread.start()

    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

    print(f"Valor final del contador: {counter}")

    # Multiprocessing (para tareas CPU-bound)
    print("\n-- Multiprocessing (para tareas CPU-bound) --")

    def run_cpu_tasks_in_processes() -> List[Tuple[int, float]]:
        """Run CPU-bound tasks using multiple processes.

        Returns:
            A list of results from each process
        """
        # Crear un pool de procesos
        with multiprocessing.Pool(processes=3) as pool:
            # Ejecutar tareas en paralelo
            results = pool.starmap(
                cpu_bound_task,
                [(i, 5000000) for i in range(3)]
            )
            return results

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        print("Ejecutando tareas CPU-bound con multiprocessing:")
        mp_start = time.time()

        # Ejecutar tareas CPU-bound en procesos separados
        try:
            mp_results = run_cpu_tasks_in_processes()
            print(f"Resultados: {mp_results}")
        except Exception as e:
            print(f"Error en multiprocessing: {e}")

        mp_end = time.time()
        print(f"Tiempo total con multiprocessing: {mp_end - mp_start:.2f} segundos")

    # Comunicación entre procesos
    print("\n-- Comunicación entre procesos --")

    def producer(queue: multiprocessing.Queue, items: int) -> None:
        """Produce items and put them in a queue.

        Args:
            queue: The queue to put items into
            items: The number of items to produce
        """
        print(f"Productor iniciado (PID: {os.getpid()})")
        for i in range(items):
            item = f"Item {i}"
            queue.put(item)
            print(f"Productor: {item} producido")
            time.sleep(0.1)
        # Señal de finalización
        queue.put(None)
        print("Productor: terminado")

    def consumer(queue: multiprocessing.Queue) -> None:
        """Consume items from a queue.

        Args:
            queue: The queue to get items from
        """
        print(f"Consumidor iniciado (PID: {os.getpid()})")
        while True:
            item = queue.get()
            if item is None:  # Señal de finalización
                break
            print(f"Consumidor: {item} consumido")
            time.sleep(0.2)
        print("Consumidor: terminado")

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        # Crear una cola para comunicación entre procesos
        queue = multiprocessing.Queue()

        # Crear procesos
        prod_process = multiprocessing.Process(target=producer, args=(queue, 5))
        cons_process = multiprocessing.Process(target=consumer, args=(queue,))

        # Iniciar procesos
        prod_process.start()
        cons_process.start()

        # Esperar a que terminen
        prod_process.join()
        cons_process.join()

    # AsyncIO (para programación asíncrona)
    print("\n-- AsyncIO (para programación asíncrona) --")

    async def async_task(task_id: int, delay: float) -> Tuple[int, float]:
        """An asynchronous task that simulates I/O operations.

        Args:
            task_id: The task identifier
            delay: The delay in seconds

        Returns:
            A tuple of (task_id, execution_time)
        """
        start_time = time.time()
        print(f"Tarea async {task_id} iniciada")
        await asyncio.sleep(delay)  # Operación asíncrona
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tarea async {task_id} completada en {execution_time:.2f} segundos")
        return task_id, execution_time

    async def main_async() -> None:
        """Main async function to run multiple async tasks."""
        # Ejecutar tareas concurrentemente
        tasks = [async_task(i, 0.5) for i in range(3)]
        results = await asyncio.gather(*tasks)
        print(f"Resultados async: {results}")

    print("Ejecutando tareas con asyncio:")
    asyncio_start = time.time()

    # Ejecutar el bucle de eventos de asyncio
    asyncio.run(main_async())

    asyncio_end = time.time()
    print(f"Tiempo total con asyncio: {asyncio_end - asyncio_start:.2f} segundos")

    # Combinando async con otras operaciones
    print("\n-- Combinando async con otras operaciones --")

    async def fetch_url(url: str) -> Tuple[str, int]:
        """Fetch a URL asynchronously using a thread pool.

        Args:
            url: The URL to fetch

        Returns:
            A tuple of (url, content_length)
        """
        print(f"Iniciando descarga de {url}")

        # Usar run_in_executor para ejecutar operaciones bloqueantes en un thread pool
        loop = asyncio.get_running_loop()

        def _fetch() -> int:
            response = requests.get(url, timeout=10)
            return len(response.content)

        try:
            content_length = await loop.run_in_executor(None, _fetch)
            print(f"Descarga de {url} completada: {content_length} bytes")
            return url, content_length
        except Exception as e:
            print(f"Error descargando {url}: {e}")
            return url, 0

    async def fetch_multiple_urls() -> None:
        """Fetch multiple URLs concurrently."""
        urls = [
            "https://www.python.org",
            "https://www.google.com",
            "https://www.github.com"
        ]

        tasks = [fetch_url(url) for url in urls]
        results = await asyncio.gather(*tasks)

        for url, size in results:
            print(f"URL: {url}, Tamaño: {size} bytes")

    print("Descargando múltiples URLs con asyncio:")
    try:
        asyncio.run(fetch_multiple_urls())
    except Exception as e:
        print(f"Error en fetch_multiple_urls: {e}")

    # concurrent.futures (API de alto nivel)
    print("\n-- concurrent.futures (API de alto nivel) --")

    def download_url(url: str) -> Tuple[str, int]:
        """Download a URL and return its content length.

        Args:
            url: The URL to download

        Returns:
            A tuple of (url, content_length)
        """
        print(f"Descargando {url}...")
        try:
            response = requests.get(url, timeout=10)
            content_length = len(response.content)
            print(f"Descarga de {url} completada: {content_length} bytes")
            return url, content_length
        except Exception as e:
            print(f"Error descargando {url}: {e}")
            return url, 0

    # Usar ThreadPoolExecutor para tareas I/O-bound
    print("\nUsando ThreadPoolExecutor para descargas:")
    urls = [
        "https://www.python.org",
        "https://www.google.com",
        "https://www.github.com"
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Iniciar las descargas y obtener futuros
        future_to_url = {executor.submit(download_url, url): url for url in urls}

        # Procesar los resultados a medida que se completan
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, size = future.result()
                print(f"Resultado para {url}: {size} bytes")
            except Exception as e:
                print(f"Error procesando {url}: {e}")

    # Usar ProcessPoolExecutor para tareas CPU-bound
    print("\nUsando ProcessPoolExecutor para tareas CPU-bound:")

    def compute_intensive_task(n: int) -> Tuple[int, float]:
        """Perform a compute-intensive task.

        Args:
            n: The task identifier and complexity factor

        Returns:
            A tuple of (task_id, result)
        """
        print(f"Tarea {n} iniciada en proceso {os.getpid()}")
        start_time = time.time()

        # Tarea intensiva en CPU
        result = sum(i * i for i in range(n * 1000000))

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Tarea {n} completada en {execution_time:.2f} segundos")
        return n, result

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        # Usar ProcessPoolExecutor para ejecutar tareas CPU-bound en paralelo
        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            tasks = [1, 2, 3]
            results = list(executor.map(compute_intensive_task, tasks))

            for n, result in results:
                print(f"Resultado de tarea {n}: {result}")

    # Patrones de concurrencia
    print("\n-- Patrones de concurrencia --")

    # 1. Patrón productor-consumidor con asyncio
    print("\n1. Patrón productor-consumidor con asyncio:")

    async def producer_async(queue: asyncio.Queue, items: int) -> None:
        """Produce items and put them in a queue asynchronously.

        Args:
            queue: The asyncio queue to put items into
            items: The number of items to produce
        """
        for i in range(items):
            item = f"Item {i}"
            await queue.put(item)
            print(f"Productor async: {item} producido")
            await asyncio.sleep(0.1)

        # Señal de finalización
        await queue.put(None)
        print("Productor async: terminado")

    async def consumer_async(queue: asyncio.Queue) -> None:
        """Consume items from a queue asynchronously.

        Args:
            queue: The asyncio queue to get items from
        """
        while True:
            item = await queue.get()
            if item is None:  # Señal de finalización
                queue.task_done()
                break

            print(f"Consumidor async: {item} consumido")
            await asyncio.sleep(0.2)
            queue.task_done()

        print("Consumidor async: terminado")

    async def producer_consumer_example() -> None:
        """Run the producer-consumer pattern with asyncio."""
        queue = asyncio.Queue()

        # Crear y ejecutar tareas
        producer_task = asyncio.create_task(producer_async(queue, 5))
        consumer_task = asyncio.create_task(consumer_async(queue))

        # Esperar a que el productor termine
        await producer_task

        # Esperar a que el consumidor procese todos los elementos
        await queue.join()

        # Esperar a que el consumidor termine
        await consumer_task

    print("Ejecutando patrón productor-consumidor con asyncio:")
    asyncio.run(producer_consumer_example())

    # 2. Patrón de trabajadores (worker pool)
    print("\n2. Patrón de trabajadores (worker pool):")

    def worker(worker_id: int, task_queue: multiprocessing.Queue, result_queue: multiprocessing.Queue) -> None:
        """Process tasks from a queue and put results in another queue.

        Args:
            worker_id: The worker identifier
            task_queue: The queue to get tasks from
            result_queue: The queue to put results into
        """
        print(f"Trabajador {worker_id} iniciado (PID: {os.getpid()})")

        while True:
            task = task_queue.get()
            if task is None:  # Señal de finalización
                print(f"Trabajador {worker_id} terminando")
                break

            # Procesar la tarea
            task_id, data = task
            print(f"Trabajador {worker_id} procesando tarea {task_id}")

            # Simular procesamiento
            time.sleep(random.uniform(0.1, 0.5))
            result = (task_id, data * 2)  # Resultado simple: duplicar el dato

            # Enviar el resultado
            result_queue.put(result)

        print(f"Trabajador {worker_id} terminado")

    def worker_pool_example() -> None:
        """Run a worker pool example with multiprocessing."""
        # Crear colas para tareas y resultados
        task_queue = multiprocessing.Queue()
        result_queue = multiprocessing.Queue()

        # Crear trabajadores
        num_workers = 3
        workers = []

        for i in range(num_workers):
            p = multiprocessing.Process(target=worker, args=(i, task_queue, result_queue))
            workers.append(p)
            p.start()

        # Enviar tareas
        num_tasks = 10
        for i in range(num_tasks):
            task = (i, random.randint(1, 100))
            task_queue.put(task)
            print(f"Tarea {i} enviada: {task}")

        # Enviar señales de finalización
        for _ in range(num_workers):
            task_queue.put(None)

        # Recoger resultados
        results = []
        for _ in range(num_tasks):
            result = result_queue.get()
            results.append(result)
            print(f"Resultado recibido: {result}")

        # Esperar a que todos los trabajadores terminen
        for p in workers:
            p.join()

        print(f"Todos los trabajadores han terminado. Resultados: {results}")

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        print("Ejecutando patrón de trabajadores con multiprocessing:")
        worker_pool_example()

    # Ejercicio: Procesamiento paralelo de imágenes (simulado)
    print("\n-- Ejercicio: Procesamiento paralelo de imágenes (simulado) --")

    def process_image(image_id: int) -> Tuple[int, str]:
        """Simulate processing an image.

        Args:
            image_id: The image identifier

        Returns:
            A tuple of (image_id, result_message)
        """
        print(f"Procesando imagen {image_id}")

        # Simular tiempo de procesamiento variable
        processing_time = random.uniform(0.2, 1.0)
        time.sleep(processing_time)

        # Simular diferentes operaciones
        operations = ["resize", "filter", "rotate", "crop"]
        operation = random.choice(operations)

        result = f"Imagen {image_id} procesada con '{operation}' en {processing_time:.2f}s"
        print(result)

        return image_id, result

    def process_images_sequential(num_images: int) -> List[Tuple[int, str]]:
        """Process images sequentially.

        Args:
            num_images: The number of images to process

        Returns:
            A list of processing results
        """
        results = []
        for i in range(num_images):
            results.append(process_image(i))
        return results

    def process_images_parallel(num_images: int) -> List[Tuple[int, str]]:
        """Process images in parallel using ProcessPoolExecutor.

        Args:
            num_images: The number of images to process

        Returns:
            A list of processing results
        """
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(process_image, range(num_images)))
        return results

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        num_images = 5

        print("\nProcesamiento secuencial:")
        start_time = time.time()
        sequential_results = process_images_sequential(num_images)
        end_time = time.time()
        print(f"Tiempo total secuencial: {end_time - start_time:.2f} segundos")

        print("\nProcesamiento paralelo:")
        start_time = time.time()
        parallel_results = process_images_parallel(num_images)
        end_time = time.time()
        print(f"Tiempo total paralelo: {end_time - start_time:.2f} segundos")


# Funciones exportables para ser utilizadas por otros módulos
def run_in_thread(func: Callable[..., Any], *args: Any, **kwargs: Any) -> threading.Thread:
    """Run a function in a separate thread.

    Args:
        func: The function to run
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function

    Returns:
        The thread object
    """
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread


def run_in_process(func: Callable[..., Any], *args: Any, **kwargs: Any) -> multiprocessing.Process:
    """Run a function in a separate process.

    Args:
        func: The function to run
        *args: Arguments to pass to the function
        **kwargs: Keyword arguments to pass to the function

    Returns:
        The process object
    """
    process = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
    process.start()
    return process


def parallel_map(func: Callable[[Any], Any], items: List[Any], max_workers: Optional[int] = None) -> List[Any]:
    """Apply a function to each item in a list in parallel.

    Args:
        func: The function to apply
        items: The list of items
        max_workers: Maximum number of workers (default: None, uses CPU count)

    Returns:
        A list of results
    """
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(func, items))
    return results


if __name__ == "__main__":
    # Este bloque permite ejecutar este módulo de forma independiente
    concurrency_examples()

    # Demostración de las funciones exportables
    print("\n-- Demostración de funciones exportables --")

    def example_function(name: str, delay: float) -> None:
        """An example function that prints a message after a delay.

        Args:
            name: A name to include in the message
            delay: The delay in seconds
        """
        print(f"Función {name} iniciada")
        time.sleep(delay)
        print(f"Función {name} completada después de {delay} segundos")

    print("\nUsando run_in_thread:")
    thread = run_in_thread(example_function, "thread_example", 0.5)
    thread.join()

    if __name__ == "__main__":  # Necesario para multiprocessing en Windows
        print("\nUsando run_in_process:")
        process = run_in_process(example_function, "process_example", 0.5)
        process.join()

        print("\nUsando parallel_map:")

        def square(x: int) -> int:
            """Square a number."""
            print(f"Calculando el cuadrado de {x} en proceso {os.getpid()}")
            time.sleep(0.2)  # Simular procesamiento
            return x * x

        numbers = [1, 2, 3, 4, 5]
        results = parallel_map(square, numbers)
        print(f"Resultados: {results}")
