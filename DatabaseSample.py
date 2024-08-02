
import time
import datetime
data = {
  "user1": {"name":'Reymart', "age":17, "birthdate":'8/6/2005'},
  "user2": {"name":'Earl',"age":16,"birthdate":'3/27/2006'}
}
class DataStoreService:
  def GetAsync(key):
    if key in data:
      return data[key]
    else:
      return False
  def GetListOfData ():
    print("data:")
    for i in data:
      birthday = ParseService.ParseDateBirth(data[i]["birthdate"])
      print(f'[ {i} = Name: {data[i]["name"]}, Age: {data[i]["age"]}, birthday: {birthday} ]')
  def SetAsync (key, value):
    if key in data:
      return False
    else:
      data[key] = value
      return True
class ParseService:
  def ParseDateBirth(stringDate):
    fil = stringDate.split("/")
    month = int(fil[0])
    day = int(fil[1])
    year = int(fil[2])
    birth = datetime.datetime(year, month, day)
    DateMonth = birth.strftime("%B")
    DateYear = birth.strftime("%Y")
    DateDay = birth.strftime("%A")
    full_date = f'{DateMonth} {day}, {DateYear}'
    return full_date
  def CalculateAge (stringData, args):
    fil = stringData.split("/")
    if len(fil) == 3 and fil[0].isnumeric()==True and fil[1].isnumeric()==True and fil[2].isnumeric()==True:
      month = int(args[0])
      day = int(args[1])
      year = int(args[2])
      birth = datetime.datetime(year, month, day)
      now = datetime.datetime.now()
      birthYear = int(birth.strftime("%Y"))
      yearNow = int(now.strftime("%Y"))
      formula = yearNow-birthYear
      filNow = str(now).split(" ")
      currentDate = filNow[0].split("-")
      
      year_now = int(currentDate[0])
      month_now = int(currentDate[1])
      day_now = int(currentDate[2])
      datern = f'{month_now} {day_now}, {year_now}'
      print("this",str(birth), birthYear)
      print("current",filNow, currentDate)
      print(datern)
      
      if (month < month_now and day_now > day):
        print(f'your age: {formula - 1}')
      else:
        print(f'your age: {formula}')
def app_start():
  print("Input command")
  res = input(': ')
  fil = res.split(" ")
  if fil[0].lower() == 'getdata' and len(fil) == 2:
    user = DataStoreService.GetAsync(fil[1])
    parse = ParseService.ParseDateBirth(user["birthdate"])
    print(f'Name: {user["name"]}\nAge: {user["age"]}\nBirthdate: {parse}\n')
  elif fil[0].lower() == 'adduser':
    print("format: {DataKey} {Name} {age} {month/day/year}")
    answ = input(": ")
    reg = answ.split(" ")
    if not len(reg) == 4:
      print("missing argument")
    else:
      if reg[1].isalpha() == False or reg[2].isnumeric() == False or len(reg[3].split("/")) == 2:
        print("error, please try again")
      else:
        newdata = {
          "name": reg[1],
          "age": reg[2],
          "birthdate": reg[3]
        }
        Set = DataStoreService.SetAsync(reg[0], newdata)
        if Set == True:
          print("Data added")
        else:
          print("Data key is already in the data")
  elif fil[0].lower() == "calculate" and fil[1].lower() == "age":
    print("Input your birthdate\nformat: month/day/year")
    answer = input("> ")
    split = answer.split("/")
    print(split)
    ParseService.CalculateAge(answer, split)
  elif fil[0].lower() == "database":
    DataStoreService.GetListOfData()
  return app_start()
app_start()