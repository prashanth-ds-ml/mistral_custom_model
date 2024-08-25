#!/bin/bash
# This script sets up the Python environment and installs dependencies

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
