

import time
import sys
import phonenumbers
import colorama
import json

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
  jsonFile = open("data.json","r")
  print(json.load(jsonFile))

functions = {
  "testfunc":{
    "function": Func1
  },
  "numberinfo":{
    "function": numberInfo
  },
  "viewdata": {
    "function": viewData
  }
}

