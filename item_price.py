# this file will open the text file and parse data into item_price_date matrix for each location then append that to the prepared csv file
import csv
from typing import Dict, Any

f = open(r"C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt", "r")
# print(f.read())

base_string = f.read()
# print(base_string)
base = base_string.split('"lineItems":[{"')

# getting '"switchableQuantity"
# this is to check items are all instock

quant2 = base[0]
import re

x = [m.start() for m in re.finditer('"switchableQuantity":', quant2)]
a, b, c = x[0], x[1], x[2]
# print(len('"switchableQuantity":21,'))
switchableQuantity = quant2[a:a + 24], quant2[b:b + 24], quant2[c:c + 24]
# print(switchableQuantity)

# also look for totalItemQuantity, to help determine if items are missing?

# use .pop to remove first or last item?
items = str(base[1])
by_item1 = items.split('"itemPrice":{"')
by_item2 = by_item1[1:]
# print(len(by_item2))
# print(by_item2[0])
# print(by_item2[-1])


# def parse_by_item:


find_prices = []
prices = []
for item in by_item2:
    num = item.find('"$')
    find_prices.append(item[num + 1:num + 15])

for item in find_prices:
    num = item.find('"')
    prices.append(item[:num-2])


find_names = []
names = []
for item in by_item2:
    num = item.find('"name"')
    find_names.append(item[num + 8:num + 100])

for item in find_names:
    # item_no_comma = item.replace(",","")
    num = item.find('"')
    names.append(item[:num])

# print(names)
name_price = dict(zip(names, prices))
#print(price_name)
from list_of_items import food_list

final_data_sorted_named_clean={}
for food_item, description in food_list.items():
    if description in name_price:
        final_data_sorted_named_clean[food_item]=name_price[description]
    else:
        final_data_sorted_named_clean[food_item] = 'item not found'
        print('not found:'+ value)


print(final_data_sorted_named_clean)
#*******print(len(final_data_sorted_named_clean))

# write function
# new list of pasrsed items
# for item in original string list
# find name
# name in food_list?
# find find price
# newlist.append name:price+/n

# variable for postcode, compair with location dictionary
# variable for num or items
# variable for date check= date from "instore pickup" less 24 hours as a check
# variable for date data created in this function

# note to self:


# how to turn file opject into workable string
# with open(r"C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt","r") as infile:
# x =infile.read
# my_list = str(infile)
# print(x)


# reader = csv.reader(infile)
# print(infile)

# cleaning notes
# 1. check for postalCode  "address":{"addressLineOne":"2200 Wheatsheaf Ln","addressLineTwo":null,"city":"Philadelphia","postalCode":"19137","state":"PA","
# 2.items devided by


# q? What does it look like if its not available at that location on that day?
