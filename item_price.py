# this file will open the text file and parse data into item_price_date matrix for each location then append that to the prepared csv file
import csv
import os.path
from os.path import exists
from typing import Dict, Any
import pandas as pd
from Location_Change import locations
from list_of_items import food_list


# def parse_by_item:
def parse_walmart_request(file_path):
    f = open(file_path, "r")

    base_string = f.read()
    base = base_string.split('"lineItems":[{"')
    items = str(base[1])
    by_item1 = items.split('"itemPrice":{"')
    by_item2 = by_item1[1:]

    find_prices = []
    prices = []
    for item in by_item2:
        num = item.find('"$')
        find_prices.append(item[num + 1:num + 15])

    for item in find_prices:
        num = item.find('"')
        prices.append(item[:num - 2])

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
    # print(price_name)
    from list_of_items import food_list

    final_data_sorted_named_clean = {}
    for food_item, description in food_list.items():
        if description in name_price:
            final_data_sorted_named_clean[food_item] = name_price[description]
        else:
            final_data_sorted_named_clean[food_item] = 'item not found'
            print('not found:' + food_item)
    f.close()
    return final_data_sorted_named_clean


v = r'''C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt'''
# print(parse_walmart_request(v))


# write to text file, then check format of text file is correct for SQL

current_date = '01232023'
current_zip_code = 19137

def add_date_to_item_price_dic(items_prices={}, date=''):
    add_date = {'date': date}
    add_date.update(items_prices)
    return add_date


def create_or_append_csv_df(zip_code,date_added={}, date=''):
    df = pd.DataFrame(date_added, index=[0])
    data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{zip_code}.csv'''

    if os.path.exists(data_in_directory):
        print(f' {zip_code} is already there')
        #append new data method here
        df.to_csv(data_in_directory, mode='a', index=1, header=False)
        pass
    else:
        df.to_csv(data_in_directory)


df_holding = parse_walmart_request(v)
date_added = add_date_to_item_price_dic(df_holding,current_date)
print(date_added)
create_or_append_csv_df(current_zip_code,date_added,current_date)
# use df_holding to make dataframe headers and first row, then add next row. I do not know if I can create csv files from here or just save to them.

# still todo - additions
# variable for "postalCode":"19137", compair with location dictionary
# variable for num or items
# variable for date check= date from "instore pickup" less 24 hours as a check
# variable for date data created in this function
# get set up in classes once functioning for better organization and function
# q? What does it look like if its not available at that location on that day?


# reader = csv.reader(infile)
# print(infile)
