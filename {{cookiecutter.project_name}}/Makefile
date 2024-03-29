PYTHON_VERSION ?= 3.10.6
CMD := poetry run
SRC_DIR := src
TESTS_DIR := tests

help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
.PHONY: help

run: ## Run as package
	$(CMD) python $(SRC_DIR)/{{cookiecutter.package_name}}
.PHONY: run

format: ## Format with Black & Isort
	$(CMD) black $(SRC_DIR) $(TESTS_DIR)
	$(CMD) isort $(SRC_DIR) $(TESTS_DIR)
.PHONY: format

lint: lint-black lint-flake lint-mypy ## Lint with Black, Flake 
.PHONY: lint

test: ## Unit test with Pytest
	$(CMD) pytest --cov=src --cov-report term --cov-report html:tests/.coverage $(TESTS_DIR)
.PHONY: test

safety: ## Dependancy security screening
	poetry export --with dev --format=requirements.txt --without-hashes | poetry run safety check --stdin

qa: safety lint test ## for CI/CD.
.PHONY: qa

qa-local: format qa
.PHONY: qa-local

lint-black:
	$(CMD) black --check --fast $(SRC_DIR) $(TESTS_DIR)
.PHONY: lint-black

lint-flake: 
	$(CMD) flakeheaven lint $(SRC_DIR) $(TESTS_DIR)
.PHONY: lint-flake

lint-mypy:
	$(CMD) mypy $(SRC_DIR)/{{cookiecutter.package_name}}
.PHONY: lint-mypy
