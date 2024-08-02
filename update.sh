


light_green='\033[1;32m'
nc='\033[0m'
printf "${light_green}pythonPractices updating...${nc}\]"
data=('phonenumbers', 'sys')
for i in "${data[@]}"
do
pkg install "${i}"
done

rm -rf
git clone https://github.com/reyyymartt/pythonPractices.git

printf "${light_green}file updated${nc}\]"
ls


exit
