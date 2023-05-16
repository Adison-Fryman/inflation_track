# file is for creating the stock availability DF from the already made txt files in directory.


import os
import item_price_parse as parse
from locations import locations_dict
import datetime

#new_list = os.listdir('C:\dev\inflation_track\walmart_cart_date.location.stock')

print(new_list)
for item in new_list:
    if item == 'grouped':
        continue
    date = item.split('.')[0]
    location = item.split('.')[1]
    print (date, location)
    text_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.stock\{date}.{location}.txt'
    raw_string = parse.parse_walmart_request(text_file_path)
    raw_items = (parse.raw_items_strings(parse.parse_walmart_request(text_file_path)))

    names = parse.get_item_names(raw_items)
    prices = parse.get_items_prices(raw_items)
    stock = parse.get_stock_availability(raw_items)

    name_stock = dict(zip(names, stock))
    name_price = dict(zip(names, prices))

    checking_postcode = parse.check_postal_code(location, raw_string)
    print(parse.postal_code_match(checking_postcode, location))

    # print(get_num_items_from_string(raw_string))
    print(parse.get_num_items_from_stock_dict(name_stock))

    x = parse.ordered_food_price_dict(name_price)
    xx = parse.add_date_to_dic(x, date)

    y = parse.ordered_name_stock_dict(name_stock)
    yy = parse.add_date_to_dic(y, date)
    # print(yy)
    parse.create_or_append_csv_df_stock(location, yy, date)



    print(parse.get_num_items_from_string(raw_string))
    print(parse.get_num_items_from_stock_dict(name_stock))
    # check post code
    print(f'location in file: {parse.check_postal_code(location, raw_string)} location intended:{location}')
    # check date-whole date- only returns date string, need to ask user if date string is ok
    print(parse.check_date(raw_string))





