
#! /bin/bash

echo "---Installing Packages---"
Packages=('phonenumbers', 'sys', 'pillow')

for package in "${Packages[@]}"
do
pkg install "${package}"
printf "${package} added"
done

echo "App starting..."
python3 numberinfo.py



