#!/bin/bash

# jupyter notebook --port 8888 --ip=0.0.0.0 --no-browser --notebook-dir=/vagrant/notebooks

ROOT_DIR=/vagrant
export PYTHONPATH=$ROOT_DIR/python
IP=$(hostname -I | awk  '{ print $2 }')

JUPYTER_CMD="jupyter lab --port=8888 --ip=$IP --no-browser"

BASIC_NOTEBOOKS=$ROOT_DIR/notebooks

$JUPYTER_CMD --notebook-dir=$BASIC_NOTEBOOKS
