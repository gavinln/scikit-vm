#!/bin/bash

# Need to install fd and fzf for this script to work
# change to child directory using fd and fzf

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "$(fd -t d . "$(realpath "$SCRIPT_DIR/..")" | fzf)" || exit
