

import json
import time, sys
import phonenumbers
import functionsModule
import dataModule
import colorama

from colorama import Fore, Back, Style
from functionsModule import functions
from dataModule import command_functions

config={
  "user": "admin",
  "dbName": "data.json"
}

def updateUser():
  with open(config["dbName"], 'r') as file:
    data=json.load(file)
    config["user"] = data["Author"]

def function(str, args):
  command_functions[str](str, args)
  
def notFunction(str, args):
  return False

decision={
  True: function,
  False: notFunction
}
updateUser()
def input_():
  inp = input(Fore.YELLOW+config["user"]+Fore.GREEN+' $ '+Style.RESET_ALL)
  split = inp.split(" ")
  args=[]
  if (split[0].lower()=="exit"):
    return False
  check=(split[0] in command_functions) or False
  for x in range(len(split)):
  	args.append(split[x].lower())
  decision[check](split[0], args)
  input_()
    
    
input_()
