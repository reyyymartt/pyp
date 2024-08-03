
#! /bin/bash

echo "---Installing Packages---"
Packages=(
  'pkg install phonenumbers',
  'pkg install sys',
  'pip install PIL'
  )

for package in "${Packages[@]}"
do
package
printf "${package} added"
done

echo "App starting..."
python3 numberinfo.py



