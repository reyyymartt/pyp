


light_green='\033[1;32m'
nc='\033[0m'

printf "${light_green}pythonPractices updating...${nc}"

rm -rf pythonPractices
git clone https://github.com/reyyymartt/pythonPractices.git
printf "${light_green}file updated${nc}"
pythonPractices
exit 1
