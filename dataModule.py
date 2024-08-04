
import functionsModule
import colorama

from functionsModule import functions
from colorama import Fore, Back, style


def ignore(str, args):
  return False

def executeFunction (str, args):
  if (len(args)>=1):
    check=(args[1] in functions) or False
    if (check==True):
      functions[args[1]]["function"](args)
    else:
      print("couldn't find["+Fore.RED+args[1]+Style.RESET_ALL+'] as a function')


command_functions {
  "exit": ignore,
  "exe": executeFunction
}
