#! /usr/bin/env bash

pyenv local
poetry install

# location of python executable
EXECUTABLE=$(poetry env info | awk '/Executable/ { print $2; exit }')

# replace the placeholder in the json file
sed -i.bak "/<interpreter_path>/ s#<interpreter_path>#$EXECUTABLE#" \
  .vscode/settings.json

# the sed program created a backup (with the `-i.bak` part). Remove it
rm .vscode/settings.json.bak
