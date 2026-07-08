#!/bin/bash

set -e

pip install -r requirements.txt

python -m playwright install chromium

echo "PLAYWRIGHT INSTALLED"
python -m playwright --version
