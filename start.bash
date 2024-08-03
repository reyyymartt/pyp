
#! /bin/bash
light_green='\e[1;32m'
yellow='\e[33m'
nc='\e[0m'

echo -e "${light_green}---Installing Packages---${nc}"

pkg install phonenumbers
pkg install sys
pip install colorama

echo -e "${yellow}All set, program started!${nc}"
python3 system.py




