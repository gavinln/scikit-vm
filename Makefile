# Using Makefiles in Python
# https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html

# Listing targets in the Makefile
# http://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile

ifeq ($(OS),Windows_NT)
    SHELL='c:/Program Files/Git/usr/bin/sh.exe'
endif

ROOT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '{if ($$1 !~ "^[#.]") {print $$1}}'

flashcards_scikit:
	@jupytext --to markdown -o scikit_flash_cards.md notebooks/12_Scikit_flash_cards.ipynb
	# @jupytext --to ipynb -o notebooks/12_Scikit_flash_cards.ipynb scikit_flash_cards.md

flashcards_python:
	@jupytext --to markdown -o python_flash_cards.md notebooks/13_Python_flash_cards.ipynb
	# @jupytext --to ipynb -o notebooks/13_Python_flash_cards.ipynb python_flash_cards.md

flashcards_algorithms:
	@jupytext --to markdown -o algorithms_flash_cards.md notebooks/14_Algorithms_flash_cards.ipynb
	# @jupytext --to ipynb -o notebooks/14_Algorithms_flash_cards.ipynb algorithms_flash_cards.md
