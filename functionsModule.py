

import time
import sys
import phonenumbers
import colorama
import json
import requests

dbName = 'data.json'

from colorama import Fore, Back, Style
from phonenumbers import timezone,geocoder,carrier

def Func1(args):
  print(Fore.RED + Back.GREEN + 'Function called' + Style.RESET_ALL)
  
def numberInfo (args):
  print("input phonenumber, with country code")
  num=input(Fore.RED+">> "+Style.RESET_ALL)
  phone = phonenumbers.parse(num)
  time = timezone.time_zones_for_number(phone)
  carry = carrier.name_for_number(phone,"en")
  country = geocoder.description_for_number(phone,"en")
  print(phone)
  print(time)
  print(carry)
  print(country)

def viewData (args):
  newName = args[2]
  with open(dbName, 'r+') as file:
    data = json.load(file)
    data["Author"] = newName
    file.seek(0)
    json.dump(data, file, indent=4)
    file.truncate
    print(data["Author"])
    
def viewAuthor (args):
  with open(dbName, 'r') as f:
    data = json.load(f)
    print(data["Author"])

def get_ip_info(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main(args):
  
    ip_address = args[2]  # Replace with the IP address you want to look up
    info = get_ip_info(ip_address)
    
    if info:
        print(f"IP Address: {info.get('ip')}")
        print(f"Hostname: {info.get('hostname')}")
        print(f"City: {info.get('city')}")
        print(f"Region: {info.get('region')}")
        print(f"Country: {info.get('country')}")
        print(f"Location: {info.get('loc')}")
        print(f"Organization: {info.get('org')}")
        print(f"Timezone: {info.get('timezone')}")
    else:
        print("Failed to get information for the given IP address.")
  

functions = {
  "testfunc":{
    "function": Func1
  },
  "numberinfo":{
    "function": numberInfo
  },
  "c-author": {
    "function": viewData
  },
  "v-author": {
    "function": viewAuthor
  },
  "get_ip_info": {
    "function": main
  }
}

