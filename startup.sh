#!/bin/bash

pwd=$(pwd)

echo "running initial script"

if [ "$pwd" = "/" ]; then
  echo "current directory is /"
  cd /vagrant || { echo "Failed to change directory"; exit 1; }
  source ~/env/bin/activate || exit 1

fi






