#!/usr/bin/env python3
"""
Python Fundamentals Guide

A comprehensive reference for Python programming fundamentals,
organized into modules by topic.

Usage:
    Run the entire guide:
    $ python main.py

    Run specific sections:
    $ python main.py --section basic_types
    $ python main.py --section flow_control
    $ python main.py --section functions
    $ python main.py --section advanced_types
    $ python main.py --section exception_handling
    $ python main.py --section object_oriented
    $ python main.py --section decorators
    $ python main.py --section concurrency

    Or import specific functions to use in your own code:
    >>> from python_guide.functions import calculate_average
    >>> calculate_average([1, 2, 3, 4, 5])
    3.0
"""

import argparse
import sys
from typing import Dict, Callable, List, Optional

# Import modules from the python_guide package
from python_guide.introduction import python_introduction
from python_guide.basic_types import basic_types
from python_guide.flow_control import flow_control
from python_guide.functions import function_examples
from python_guide.advanced_types import advanced_types
from python_guide.exception_handling import exception_handling
from python_guide.object_oriented import object_oriented
from python_guide.decorators import decorators_examples
from python_guide.concurrency import concurrency_examples


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments.

    Returns:
        Parsed arguments namespace
    """
    parser = argparse.ArgumentParser(
        description="Python Fundamentals Guide",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    Run the entire guide:
    $ python main.py

    Run a specific section:
    $ python main.py --section basic_types
    $ python main.py --section flow_control
    $ python main.py --section functions
    $ python main.py --section advanced_types
    $ python main.py --section exception_handling
    $ python main.py --section object_oriented
    $ python main.py --section decorators
    $ python main.py --section concurrency
    """
    )

    parser.add_argument(
        "--section",
        type=str,
        choices=[
            "introduction",
            "basic_types",
            "flow_control",
            "functions",
            "advanced_types",
            "exception_handling",
            "object_oriented",
            "decorators",
            "concurrency"
        ],
        help="Run only a specific section of the guide"
    )

    return parser.parse_args()


def main() -> None:
    """Main entry point of the application.

    Execute all example functions to demonstrate Python concepts,
    or run a specific section based on command line arguments.
    """
    print("=" * 50)
    print("      PYTHON: GUÍA PRÁCTICA DE REFERENCIA")
    print("=" * 50)
    print(f"Ejecutando con Python {sys.version.split()[0]}")
    print("=" * 50)

    # Define mapping of section names to their functions
    sections: Dict[str, Callable[[], None]] = {
        "introduction": python_introduction,
        "basic_types": basic_types,
        "flow_control": flow_control,
        "functions": function_examples,
        "advanced_types": advanced_types,
        "exception_handling": exception_handling,
        "object_oriented": object_oriented,
        "decorators": decorators_examples,
        "concurrency": concurrency_examples
    }

    # Parse arguments
    args = parse_arguments()

    # Run specific section or all sections
    if args.section:
        if args.section in sections:
            sections[args.section]()
        else:
            print(f"Error: Sección '{args.section}' no válida.")
            sys.exit(1)
    else:
        # Run all sections in sequence
        for section_name, section_func in sections.items():
            print(f"\n\n{'=' * 30}")
            print(f"  SECCIÓN: {section_name.upper()}")
            print(f"{'=' * 30}")
            section_func()

    print("\n" + "=" * 50)
    print("      FIN DE LA GUÍA")
    print("=" * 50)


if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el script se ejecuta directamente,
    no cuando se importa como módulo.
    """
    main()
