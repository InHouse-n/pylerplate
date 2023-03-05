import os

from src import logger_provider
from src.{{cookiecutter.prackage_name}}.person import Person
from src.config import Config



def main(config: Config):
    """Small example of code to get you started"""

    print(config.test)
    karen = Person("Karen", 26, "blue")

    karen.present_yourself()

    karen.birthday()
    karen.change_name("Hanne")
    karen.present_yourself()