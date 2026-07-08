#!/bin/bash

set -e

echo "INSTALL DEPENDENCIES"

pip install -r requirements.txt

echo "INSTALL PLAYWRIGHT CHROMIUM"

python -m playwright install --with-deps chromium

echo "BUILD COMPLETE"
