#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
# pip install -r  requirements.txt

python3.7 -m pip install --upgrade pip

python manage.py collectstatic --no-input
python manage.py migrate