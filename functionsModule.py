

import time
import sys
import phonenumbers
import colorama
import json
import requests
import socket
import pywifi
import os
import tabulate

dbName = 'data.json'

from colorama import Fore, Back, Style
from phonenumbers import timezone,geocoder,carrier
from pywifi import PyWiFi, const, Profile
from tabulate import tabulate

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

def get_local_ip(args):
    hostname = socket.gethostname()  # Get the hostname of the machine
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)# Get the IP address associated with the hostname
    return local_ip

def get_public_ip(args):
    response = requests.get('https://api.ipify.org?format=json')  # Call an external service to get the public IP address
    public_ip = response.json().get('ip')
    print(public_ip)
    return public_ip

if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"Local IP Address: {local_ip}")
    try:
        public_ip = get_public_ip()
        print(f"Public IP Address: {public_ip}")
    except Exception as e:
        print(f"Could not retrieve public IP: {e}")
      
def list_of_functions(args):
  table = []
  for i in functions:
    funcText = Fore.YELLOW + function[i]["function"].__name__ +'()'+Style.RESET_ALL
    table.append([functions[i],funcText])
    
  finishProduct=tabulate(table,headers=['Command Name', 'Inner Function'])
  print(finishProduct)
  
def scan_wifi():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first wireless interface

    iface.scan()  # Start scanning
    time.sleep(5)  # Wait for the scan to complete

    scan_results = iface.scan_results()  # Get the scan results
    networks = []

    for network in scan_results:
        ssid = network.ssid
        bssid = network.bssid
        signal = network.signal
        auth = network.akm[0] if network.akm else "Unknown"
        cipher = network.cipher if network.cipher else "Unknown"
        networks.append({'SSID': ssid, 'BSSID': bssid, 'Signal': signal, 'Auth': auth, 'Cipher': cipher})

    return networks

def scanNets(args):
    networks = scan_wifi()
    print("Available WiFi networks:")
    for network in networks:
        print(f"SSID: {network['SSID']}, BSSID: {network['BSSID']}, Signal: {network['Signal']}, Auth: {network['Auth']}, Cipher: {network['Cipher']}")

  
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
  },
  "my_public_ip": {
    "function": get_public_ip
  },
  "my_private_ip": {
    "function": get_local_ip
  },
  "f-list": {
    "function": list_of_functions
  },
  "swn": {
    "function": scanNets
  }
}

