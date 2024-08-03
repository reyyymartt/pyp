

import time
import sys
import phonenumbers
import colorama

from colorama import Fore, Back, Style


def Func1(args):
  print(Fore.RED + Back.GREEN + 'Function called' + Style.RESET_ALL)
  print(args)


functions = {
"func1":{
"func": Func1
}
}
