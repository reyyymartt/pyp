


light_green='\033[1;32m'
nc='\033[0m'

cd
printf "${light_green}pythonPractices updating...${nc}"

git remote update
printf "${light_green}file updated${nc}"
ls
printf "${light_green}exit${nc}"

exit 1
