#!/bin/bash
set -e
python -m venv ci_env
source ci_env/bin/activate
pip install --upgrade cynthion/python/.[gateware,gateware-soc]
deactivate
