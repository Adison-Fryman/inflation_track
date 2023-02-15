import os.path
import pandas as pd
import datetime
from datetime import timedelta
from typing import Dict

from list_of_items import food_list


# obtain string and parse request into usable chunks for reuse in other functions
def parse_walmart_request(file_path):
    f = open(file_path, "r")
    base_string = f.read()
    f.close()
    return base_string


# this function is the base split of the data, it creates a list of strings that is later used in several other functions. shadow name: raw_items
def raw_items_strings(base):
    base_list = base.split('"lineItems":[{"')
    items = str(base_list[1])
    split_up = items.split('"itemPrice":{"')
    # remove starting text
    return split_up[1:]


def get_items_prices(raw_items: list):
    if raw_items is None:
        raw_items = []
    find_prices = []
    prices = []
    for item in raw_items:
        index = item.find('"$')
        find_prices.append(item[index + 1:index + 15])

    for item in find_prices:
        index = item.find('"')
        prices.append(item[:index - 2])

    return prices


def get_item_names(raw_items: list):
    find_names = []
    names = []
    for item in raw_items:
        index = item.find('"name"')
        find_names.append(item[index + 8:index + 100])

    for item in find_names:
        # item_no_comma = item.replace(",","")
        index = item.find('"')
        names.append(item[:index])

    return names


def check_date(raw_string):
    # delivery date, check that it is near today's date for file writing. Don't let file be writen if dates are too far apart.
    # for now the function returns a date string that the user will be able to confirm
    # once confirmed file will be writen with todays date
    string = raw_string
    date1 = datetime.date.today()
    tomorrow = date1 + timedelta(1)
    today_date = date1.strftime("%Y-%m-%d")
    thisMonth_date = date1.strftime("%Y-%m")
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")
    date_string = ''
    if string.find(today_date) != -1:
        print("todays date found in string below:")
        index = string.find(str(today_date))
        date_string += string[index - 30:index + 200]
    elif string.find(str(tomorrow_date)) != -1:
        print("tomorrow's date found in string below:")
        index = string.find(str(thisMonth_date))
        date_string += string[index - 30:index + 200]
    else:
        print("Today's date not found.")
        print("Tomorrow's date not found.")
        print(' Only date found was:')
        index = string.find(str(thisMonth_date))
        date_string += string[index - 30:index + 200]
        # put a way to exit/ask if this date is ok
    return date_string



def check_postal_code(postal_code: int, raw_string: str):
    # get postal code from file and check against expected post code from locations_dict. DO NOT ALLOW INCORRECT ANSWERS
    string = raw_string
    postcode_string = ''
    if string.find(str(postal_code)) == -1:
        postcode_string = False
    elif string.find(str(postal_code)) != -1:
        index = string.find(str(postal_code))
        postcode_string += string[index:index + 5]

    return postcode_string



def get_stock_availability(raw_items: list):
    find_stock = []
    status = '''availabilityStatus":"OUT_OF_STOCK'''
    for item in raw_items:
        if status in item:
            find_stock.append('NO')
        else:
            find_stock.append('YES')

    return find_stock

#def get_num_items(stock_dict, raw_string, expected_num_items):
def get_num_items_from_string(raw_string):
    # check that the list is the right length and so is the quantity. use the check stock to count yes vrs no as well as the number provided in string
    # string    {"subTotal":{"label":"Subtotal (17 items)"," or totalItemQuantity":17
    # string    ":[{"code":"OUT_OF_STOCK","shouldDisableCheckout":false,"itemIds":["8421ff2b-e38b-4a8e-b2a9-c07e5042495d","57d2a76f-ab3a-4e9b-98cb-01969da02722","dd8211c3-10e5-44bd-a5dc-16a60f15c7ba"],
    #fix this to try for "out of stock" if false just do items_string_index
    #Should be in if/else or try/expt incase it throws an error
    items_string_index =(raw_string.find('totalItemQuantity'))
    items_string = raw_string[(items_string_index+19):(items_string_index+21)]
    out_of_stock_id_index = raw_string.find('{"code":"OUT_OF_STOCK"')
    out_of_stock_string = raw_string[(out_of_stock_id_index+19):]
    index1_itemIds =int(out_of_stock_string.find('['))
    index2_itemIds =int(out_of_stock_string.find(']'))
    num_itemIds = len((out_of_stock_string[index1_itemIds+1 : index2_itemIds]).split(","))
    #print(items_string)
    #print(num_itemIds)
    return int(items_string) + num_itemIds

def get_num_items_from_stock_dict(stock_dict:dict):
    yeses = 0
    nos = 0
    other = 0
    for status in stock_dict.values():
        if status == 'YES':
            yeses += 1
        elif status == "NO":
            nos += 1
        else:
            other +=1

    total = yeses+nos
    errors = other
    return f'Total:{total}   Number of In Stock Items: {yeses}  Number Out of Stock: {nos}  Errors: {errors}'

def ordered_food_price_dict(name_price: dict):
    final_data_sorted_named_clean = {}
    for food_item, description in food_list.items():
        # locates the most important word of the food description:
        # (incase the description changes over time)
        food_item_words = food_item.lower().split()
        food_item_key_word = food_item_words[-1]
        # checking the item description in food_item against the parsed description:
        # if description is found, price is placed in dict with name:
        if description in name_price:
            final_data_sorted_named_clean[food_item] = name_price[description]
        # if description is not found, food item key word is used instead.
        elif food_item_key_word in str(name_price).lower():
            res = [name for name, price in name_price.items() if food_item_key_word in name.lower()]
            final_data_sorted_named_clean[food_item] = name_price[res[0]]
        # if neither of those works user is alerted (in future will ask user to enter price manually)
        else:
            final_data_sorted_named_clean[food_item] = 'item not found'
            print('not found:' + food_item)
        # print(food_item_last_word)
    return final_data_sorted_named_clean

def ordered_name_stock_dict(name_stock: dict):
    pass

def add_date_to_item_price_dic(items_prices: dict, date: str):
    add_date: dict[str, str] = {'date': date}
    add_date.update(items_prices)
    return add_date


def create_or_append_csv_df(zip_code, date_added: dict, date: str):
    df = pd.DataFrame(date_added, index=[0])
    data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{zip_code}.csv'''

    if os.path.exists(data_in_directory):
        print(f" {zip_code} is has been updated, with prices from today's date: {date}")
        # print( number of items:, items out of stock?)

        df.to_csv(data_in_directory, mode='a', index=1, header=False)
        pass
    else:
        df.to_csv(data_in_directory)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #change these below when testing.
    current_date = '20230213'
    current_zip_code = 49548
    #good idea to add test to path_temp
    path_temp = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\{current_date}.{current_zip_code}.txt'''
    raw_string = parse_walmart_request(path_temp)
    #print(raw_string)
    raw_items = (raw_items_strings(parse_walmart_request(path_temp)))
    # print(raw_items)
    names = get_item_names(raw_items)
    prices = get_items_prices(raw_items)
    stock = get_stock_availability(raw_items)

    name_stock = dict(zip(names, stock))
    name_price = dict(zip(names, prices))
    # print(name_price)
    # print(name_stock)
    checking_date = check_date(raw_string)
    print(checking_date)
    checking_postcode = check_postal_code(current_zip_code,raw_string)
    #print(checking_postcode)
    #print(get_num_items_from_string(raw_string))
    print(get_num_items_from_stock_dict(name_stock))
    x = ordered_food_price_dict(name_price)
    # print(x)
    # create_or_append_csv_df(current_zip_code,add_date_to_item_price_dic(x,current_date))
