
import functionsModule
import colorama
import subprocess
import pyptools

from functionsModule import functions, searCH, viewAuthor
from colorama import Fore, Back, Style
from pyptools import *

def ignore(str, args):
  user=viewAuthor({})
  print(f"logged out as {user}")
  exit()
def runPro(str, args):
  run=[]
  if (len(args)>0):
    for x in range(1,len(args)):
      run.append(args[x])
    subprocess.run(run)
  else:
    colored=colortext("missing arguments")
    bold=boldtext(colored)
    print(bold)
  
def executeFunction (str, args):
  user=viewAuthor({})
  if (len(args)>1):
    check=(args[1] in functions) or False
    if (check==True):
      functions[args[1]]["function"](args)
      text = f"{colortext(user,"magenta")} has called the function {args[1]}"
      log(text)
    else:
      print("no function called {"+Fore.RED+args[1]+Style.RESET_ALL+'}')
      table=[]
      for x in functions:
        table.append(x)
      search=searCH(table,args[1])
      if (len(search)>0):
        for a in search:
          text = colortext(a,"green")
          bd=boldtext(text)
          print("Did you mean "+bd)

command_functions={
  "logout": ignore,
  "exe": executeFunction,
  "run": runPro
}
