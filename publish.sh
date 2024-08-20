#!/bin/sh

rm dist/*

# Ubuntu 22.04
#pip install build twine
#python -m build
#python -m twine upload dist/*

# Ubuntu 24.04
pip install pipx
pipx install build
pipx run build
pipx install twine
pipx run twine upload dist/*
