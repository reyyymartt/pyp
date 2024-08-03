
#! /bin/bash

echo "---Installing Packages---"

pkg install phonenumbers
pkg install sys
pip install PIL

echo "App starting..."
python3 numberinfo.py



