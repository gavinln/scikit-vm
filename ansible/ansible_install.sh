#!/bin/bash
#

# Detect package management system.
YUM=$(which yum 2>/dev/null)
APT_GET=$(which apt-get 2>/dev/null)
ANSIBLE_VERSION=2.7.9

# Install Ansible and its dependencies if it's not installed already.
if ! command -v ansible >/dev/null; then
  echo "Installing Ansible dependencies and Git."
  if [[ ! -z ${YUM} ]]; then
    yum install -y git
    # yum install -y python3 python3-devel
    # yum install -y libffi-devel
    # yum install -y openssl-devel
  elif [[ ! -z ${APT_GET} ]]; then
    apt-get install -y git
    apt-get install -y python3-distutils
    # apt-get install -y python3 python3-dev
    # apt-get install -y libffi-dev
    # apt-get install -y libssl-dev
  else
    echo "Neither yum nor apt-get are available."
    exit 1;
  fi

  echo "Installing pip."
  wget https://bootstrap.pypa.io/get-pip.py
  python3 get-pip.py && rm -f get-pip.py

  # Install GCC / required build tools.
  # if [[ ! -z $YUM ]]; then
  #   yum install -y gcc
  # elif [[ ! -z $APT_GET ]]; then
  #   apt-get install -y build-essential
  # fi

  echo "Installing required python modules."
  # pip install paramiko pyyaml jinja2 markupsafe

  echo "Installing Ansible."
  pip install ansible==$ANSIBLE_VERSION
fi
