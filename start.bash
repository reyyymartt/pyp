
#! /bin/bash

echo "---Installing Packages---"
Packages=('phonenumbers', 'sys', 'PIL')

for package in "${Packages[@]}"
do
pkg install "${package}"
printf "${package} added"
done

echo "App starting..."
python3 numberinfo.py



