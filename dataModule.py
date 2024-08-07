
import functionsModule
import colorama

from functionsModule import functions, searCH
from colorama import Fore, Back, Style


def logoutApp():
  print("end")

def ignore(str, args):
  logoutApp()

def executeFunction (str, args):
  if (len(args)>1):
    check=(args[1] in functions) or False
    if (check==True):
      functions[args[1]]["function"](args)
    else:
      print("no function called {"+Fore.RED+args[1]+Style.RESET_ALL+'}')
      table=[]
      for x in functions:
        table.append(x)
      search=searCH(table,args[1])
      if (len(search)>0):
        for a in search:
          print("Did you mean "+Fore.YELLOW+a+Style.RESET_ALL+"?")

command_functions={
  "exit": ignore,
  "exe": executeFunction
}
