

import json
import time, sys
import phonenumbers
import functionsModule
import colorama
from colorama import Fore, Back, Style
from functionsModule import functions

def input_():
  inp = input(Fore.YELLOW+'admin'+Fore.GREEN+' $ '+Style.RESET_ALL)
  split = inp.split(" ")
  arguments=[]
  for x in range(len(split)):
  	arguments.append(split[x].lower())
  if (split[0]=="exit"):
    return False
  elif(split[0]=="exec" and len(split)>=2):
    if (split[1].lower() in functions):
    	functions[split[1].lower()]["func"](arguments)
    else:
    	print(split[1],"not found")
    
    
  input_()
    
    
input_()
