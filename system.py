

import json
import time, sys
import phonenumbers
import functionsModule
import dataModule
import colorama
import PIL

from PIL import Image
from colorama import Fore, Back, Style
from functionsModule import functions
from dataModule import command_functions

def load_and_display_image(image_path):
    # Load the image
    img = Image.open(image_path)
    # Display the image
    img.show()
  

def function(str, args):
  command_functions[str](str, args)
  
def notFunction(str, args):
  return False

decision={
  True: function,
  False: notFunction
}
load_and_display_image("show.jpg")
def input_():
  inp = input(Fore.YELLOW+'admin'+Fore.GREEN+' $ '+Style.RESET_ALL)
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
