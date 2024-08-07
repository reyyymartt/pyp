

import json
import time, sys
import phonenumbers
import functionsModule
import colorama
import fontstyle

from colorama import Fore, Back, Style

def colortext(text, color):
	colorList={
	"red": Fore.RED,
	"yellow": Fore.YELLOW,
	"green": Fore.GREEN,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN
	}
	if (color in colorList):
		return colorList[color]+text+Style.RESET_ALL
	else:
		None
		
def boldtext(text):
	return fontstyle.apply(text, 'bold')
