# Listing targets in the Makefile
# http://stackoverflow.com/questions/4219255/how-do-you-get-the-list-of-targets-in-a-makefile

SCRIPT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

.DEFAULT_GOAL=help
.PHONY: help
help:  ## help for this Makefile
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

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

jupyter:  ## run jupyter
	# pipenv run bash ./scripts/lab-jupyter.sh
	pipenv run bash ./scripts/notebook-jupyter.sh

tmux:
	tmuxp load tmux.yaml
