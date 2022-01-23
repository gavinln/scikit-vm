#!/bin/bash

# Script helps run a Makefile from any sub-directory
# non-file arguments are passed to Makefile directly
# file arguments are converted to relative paths

set -Eeuo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
MAKEFILE_DIR=$(realpath "$SCRIPT_DIR/..")

make -C "$MAKEFILE_DIR" "$@"
