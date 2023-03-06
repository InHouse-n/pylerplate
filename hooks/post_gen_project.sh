#! /usr/bin/env bash

pyenv local

poetry install

git init
git add .
git commit -m "generate project with cookiecutter"