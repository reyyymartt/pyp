

import time
import sys
import phonenumbers
import colorama
import json

dbName = 'data.json'

from colorama import Fore, Back, Style
from phonenumbers import timezone,geocoder,carrier

def Func1(args):
  print(Fore.RED + Back.GREEN + 'Function called' + Style.RESET_ALL)
  
def numberInfo (args):
  print("input phonenumber, with country code")
  num=input(Fore.RED+">> "+Style.RESET_ALL)
  phone = phonenumbers.parse(num)
  time = timezone.time_zones_for_number(phone)
  carry = carrier.name_for_number(phone,"en")
  country = geocoder.description_for_number(phone,"en")
  print(phone)
  print(time)
  print(carry)
  print(country)

def viewData (args):
  newName = args[2]
  with open(dbName, 'r+') as file:
    data = json.load(file)
    data["Author"] = newName
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate
    print(data["Author"])
    
def viewAuthor (args):
  with open(dbName, 'r') as f:
    data = json.load(f)
    print(data["Author"])

functions = {
  "testfunc":{
    "function": Func1
  },
  "numberinfo":{
    "function": numberInfo
  },
  "c-author": {
    "function": viewData
  },
  "v-author": {
    "function": viewAuthor
  }
}

