#!/bin/bash

set -e

echo "INSTALL PYTHON PACKAGES"

pip install -r requirements.txt

echo "INSTALL PLAYWRIGHT BROWSER"

python -m playwright install chromium

echo "BUILD COMPLETE"
