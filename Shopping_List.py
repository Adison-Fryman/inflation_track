
#****temp holding place for quick in project tests
# this file will add the shopping list item by item.

import re
import pandas as pd
from Location_Change import locations

import os.path
#print(os.path.exists('C:\\'))


data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\19137.csv'''
file_location = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped'''

#print(os.path.exists("walmart_cart_date.location.price\grouped"))
#print(os.listdir("walmart_cart_date.location.price\grouped"))


print(os.path.exists(data_in_directory))
print(os.listdir(file_location))

for location in locations:
    print( os.path.exists(fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{location}.csv'''))
