


light_green='\033[1;32m'
nc='\033[0m'
printf "${light_green}system updating...${nc}"

cd
rm -rf pyp
git clone https://github.com/reyyymartt/pyp.git

printf "${light_green}file updated${nc}"
cd pyp
ls


exit 1


