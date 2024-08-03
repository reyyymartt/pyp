


import os
import time
import Pillow
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from pillow import Image
im = Image.open("hopper.ppm")

im.show()

print("Input your phone number")
num = input("Phone number: ")

phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
carry = carrier.name_for_number(phone,"en")
country = geocoder.description_for_number(phone,"en")


print(phone)
print(time)
print(carry)
print(country)