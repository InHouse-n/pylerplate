import os

from src import logger_provider
from src.{{cookiecutter.package_name}}.person import Person


def main():
    """Small example of code to get you started"""

    karen = Person("Karen", 26, "blue")
    karen.present_yourself()

    karen.birthday()
    karen.change_name("Hanne")
    karen.present_yourself()