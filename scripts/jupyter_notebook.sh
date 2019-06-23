#!/bin/bash

# jupyter notebook --port 8888 --ip=0.0.0.0 --no-browser --notebook-dir=/vagrant/notebooks

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ROOT_DIR=/vagrant
export PYTHONPATH=$ROOT_DIR/python
IP=$(hostname -I | awk  '{ print $2 }')

JUPYTER_CMD="jupyter notebook --port=8888 --ip=$IP --no-browser"

BASIC_NOTEBOOKS=$SCRIPT_DIR/../notebooks

$JUPYTER_CMD --notebook-dir=$BASIC_NOTEBOOKS
