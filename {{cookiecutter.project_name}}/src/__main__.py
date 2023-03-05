import os

import click

from src import logger_provider
from src.{{cookiecutter.package_name}} import main as script

_logger = logger_provider.get_logger(__name__)


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prd"], case_sensitive=False),
    default="local",
)
def main(env: str):
    script.main()


if __name__ == "__main__":
    main()
