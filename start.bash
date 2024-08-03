
#! /bin/bash

echo "---Installing Packages---"
Packages=('phonenumbers', 'sys', 'Pillow')

for package in "${Packages[@]}"
do
pip install "${package}"
printf "${package} added"
done

echo "App starting..."
python3 numberinfo.py



