
#! /bin/bash

echo "---Installing Packages---"

pkg install phonenumbers
pkg install sys
pip install Pillow

echo "App starting..."
python3 numberinfo.py



