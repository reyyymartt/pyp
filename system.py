

import json
import time, sys
import phonenumbers
import functionsModule
import dataModule
import colorama

from colorama import Fore, Back, Style
from functionsModule import functions


def run_com (args):
  first_[]

def function():
  pass
  
def notFunction (args):
  pass
  
def executeFunction (args):
  
  
first_={
  "exit": {
    "run": run_com
  },
  "exec": {
    "run": executeFunction
  },
  
}

decision={
  True: function,
  False: notFunction
}

def input_():
  inp = input(Fore.YELLOW+'admin'+Fore.GREEN+' $ '+Style.RESET_ALL)
  split = inp.split(" ")
  arguments=[]
  check=(split[0] in first_) or False
  for x in range(len(split)):
  	arguments.append(split[x].lower())
  
  decision[check](arguments)
  input_()
    
    
input_()
