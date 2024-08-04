

import json
import time, sys
import phonenumbers
import functionsModule
import dataModule
import colorama

from colorama import Fore, Back, Style
from functionsModule import functions
from dataModule import command_functions

def function(str, args):
  command_functions[str](args)
  
def notFunction(str, args):
  print("uknown command = "+Fore.RED+str+Style.RESET_ALL)

decision={
  True: function,
  False: notFunction
}

def input_():
  inp = input(Fore.YELLOW+'admin'+Fore.GREEN+' $ '+Style.RESET_ALL)
  split = inp.split(" ")
  args=[]
  check=(split[0] in command_functions) or False
  for x in range(len(split)):
  	arguments.append(split[x].lower())
  decision[check](split[0], args)
  input_()
    
    
input_()
