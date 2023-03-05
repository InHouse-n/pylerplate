import os

import click

from src import logger_provider
from src.{{cookiecutter.package_name}} import main as script
from src import config

_logger = logger_provider.get_logger(__name__)


@click.command()
@click.option(
    "--env",
    type=click.Choice(["local", "dev", "prd"], case_sensitive=False),
    default="local",
)
def main(env: str):
    _logger.info(f"Running main script with env: {env}")
    script.main(config.get_config(env))


if __name__ == "__main__":
    main()
