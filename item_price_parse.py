import os.path
import pandas as pd
import datetime
from datetime import timedelta
# from typing import Dict

from list_of_items import food_list


# obtain string and parse request into usable chunks for reuse in other functions
def continue_yes_no():
    # answer = input('would you like to continue Y/N:')
    # if answer.upper() == 'Y':
    # option to break out of loop and exit program. (break)
    # option to skip current location and move on to next.(continue)
    # option to re-enter string (humm?)
    pass


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
    # delivery date, check that it is near today's date for file writing.
    # Don't let file be writen if dates are too far apart.
    string = raw_string
    date1 = datetime.date.today()
    tomorrow = date1 + timedelta(1)
    today_date = date1.strftime("%Y-%m-%d")
    thisMonth_date = date1.strftime("%Y-%m")
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")
    date_string = ''
    if string.find(today_date) != -1:
        print("Today's date found in string below:")
        index = string.find(str(today_date))
        date_string += string[index - 30:index + 200]
    elif string.find(str(tomorrow_date)) != -1:
        print("Tomorrow's date found in string below:")
        index = string.find(str(thisMonth_date))
        date_string += string[index - 30:index + 200]
    elif string.find(str(thisMonth_date)) != -1:
        print("Today's date not found.")
        print("Tomorrow's date not found.")
        print(' Only date found was:')
        index = string.find(str(thisMonth_date))
        date_string += string[index - 30:index + 200]
        # put a way to exit/ask if this date is ok
    else:
        print('No date found')
        ###log entered here (DATE ERROR{location})
    date_string += "\n"
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


def postal_code_match(postalcode_string: str, location):
    if int(postalcode_string) == int(location):
        return f'{postalcode_string} matches {location}, continuing with program...'
    else:
        return f'{postalcode_string} does not match {location}!'
        ####log entered here (Location ERROR f'{postalcode_string} does not match {location}!')
        # continue_yes_no()


def get_stock_availability(raw_items: list):
    find_stock = []
    status = '''availabilityStatus":"OUT_OF_STOCK'''
    for item in raw_items:
        if status in item:
            find_stock.append('NO')
        else:
            find_stock.append('YES')

    return find_stock


# *********this only works in a few situations, it is out of use for now.
def get_num_items_from_string(raw_string):
    # check that the list is the right length and so is the quantity.
    # string    {"subTotal":{"label":"Subtotal (17 items)"," or totalItemQuantity":17
    # string    ":[{"code":"OUT_OF_STOCK","shouldDisableCheckout":false,"itemIds":["8421ff2b-e38b-4a8e-b2a9-c07e5042495d","57d2a76f-ab3a-4e9b-98cb-01969da02722","dd8211c3-10e5-44bd-a5dc-16a60f15c7ba"],
    items_string_index = (raw_string.find('totalItemQuantity'))
    items_string = raw_string[(items_string_index + 19):(items_string_index + 21)]
    out_of_stock_id_index = raw_string.find('{"code":"OUT_OF_STOCK"')
    out_of_stock_string = raw_string[(out_of_stock_id_index + 19):]
    index1_itemIds = int(out_of_stock_string.find('['))
    index2_itemIds = int(out_of_stock_string.find(']'))
    num_itemIds = len((out_of_stock_string[index1_itemIds + 1: index2_itemIds]).split(","))
    return int(items_string) + num_itemIds


def get_num_items_from_stock_dict(stock_dict: dict):
    yeses = 0
    nos = 0
    other = 0
    for status in stock_dict.values():
        if status == 'YES':
            yeses += 1
        elif status == "NO":
            nos += 1
        else:
            other += 1
            ###enter log here (Item number error location,f'Total:{total}   Number of In Stock Items: {yeses}  Number Out of Stock: {nos}  Errors: {errors} )

    total = yeses + nos
    errors = other
    return f'Total:{total}   Number of In Stock Items: {yeses}  Number Out of Stock: {nos}  Errors: {errors}'


def ordered_food_price_dict(name_price: dict):
    final_data_sorted_named_clean = {}
    invalid_descriptions = 0
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
            ###enter log here (description for {food_item} in list of items is not valid today)
            invalid_descriptions += 1
        # if neither of those works user is alerted (in future will ask user to enter price manually)
        else:
            final_data_sorted_named_clean[food_item] = 'item not found'
            print('not found:' + food_item)
            ###enter log here ('not found:' + {food_item})
            invalid_descriptions += 1

    ####enter log here(f' the number of invalid descriptions in list_of_items is: {invalid_descriptions}
    return final_data_sorted_named_clean


def ordered_name_stock_dict(name_stock: dict):
    final_data_sorted_named_clean = {}
    for food_item, description in food_list.items():
        # locates the most important word of the food description:
        # (incase the description changes over time)
        food_item_words = food_item.lower().split()
        food_item_key_word = food_item_words[-1]
        # checking the item description in food_item against the parsed description:
        # if description is found, price is placed in dict with name:
        if description in name_stock:
            final_data_sorted_named_clean[food_item] = name_stock[description]
        # if description is not found, food item key word is used instead.
        elif food_item_key_word in str(name_stock).lower():
            res = [name for name, status in name_stock.items() if food_item_key_word in name.lower()]
            final_data_sorted_named_clean[food_item] = name_stock[res[0]]
            ###enter log here (description for {food_item} in list of items is not valid today)
        # if neither of those works user is alerted (in future will ask user to enter price manually?)
        else:
            final_data_sorted_named_clean[food_item] = 'item not found'
            print('not found:' + food_item)
            ###enter log here ('not found:' + {food_item})
    return final_data_sorted_named_clean


def add_date_to_dic(items_prices: dict, date: str):
    add_date: dict[str, str] = {'date': date}
    add_date.update(items_prices)
    return add_date


def create_or_append_csv_df(zip_code, date_added: dict, date: str):
    df = pd.DataFrame(date_added, index=[0])
    data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{zip_code}.csv'''

    if os.path.exists(data_in_directory):
        print(f" {zip_code} prices have been updated, with prices from today's date: {date}")
        print(f'File saved to: {data_in_directory}')
        ####ENTER LOG HERE
        df.to_csv(data_in_directory, mode='a', index=1, header=False)
        pass
    else:
        df.to_csv(data_in_directory)
        ####ENTER LOG HERE


def create_or_append_csv_df_stock(zip_code, date_added: dict, date: str):
    df = pd.DataFrame(date_added, index=[0])
    data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.stock\grouped\{zip_code}.csv'''

    if os.path.exists(data_in_directory):
        print(f" {zip_code} stock has been updated, with stock status from today's date: {date}")
        print(f'File saved to: {data_in_directory}')
        df.to_csv(data_in_directory, mode='a', index=1, header=False)
        ####ENTER LOG HERE
        pass
    else:
        df.to_csv(data_in_directory)
        ####ENTER LOG HERE


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_zip_code = 49548

    date1 = datetime.date.today()
    today_date = date1.strftime("%Y%m%d")


    def create_txt_files_test(location, date):
        # update this so that it does not overwrite files that already exist.?
        request_string = input(fr"When ready put the network request for {location} here as a string :")
        with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\{date}.{location}_test.txt',
                  'w') as new_file_name:
            print(request_string, file=new_file_name)


    create_txt_files_test(current_zip_code, today_date)
    path_temp = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\{today_date}.{current_zip_code}_test.txt'''
    raw_string = parse_walmart_request(path_temp)
    raw_items = (raw_items_strings(parse_walmart_request(path_temp)))

    names = get_item_names(raw_items)
    prices = get_items_prices(raw_items)
    stock = get_stock_availability(raw_items)

    name_stock = dict(zip(names, stock))
    name_price = dict(zip(names, prices))

    checking_postcode = check_postal_code(current_zip_code, raw_string)
    print(postal_code_match(checking_postcode, current_zip_code))

    print(check_date(raw_string))

    # print(get_num_items_from_string(raw_string))
    print(get_num_items_from_stock_dict(name_stock))

    x = ordered_food_price_dict(name_price)
    xx = add_date_to_dic(x, today_date)
    # print(xx)
    create_or_append_csv_df(current_zip_code, xx, today_date)

    y = ordered_name_stock_dict(name_stock)
    yy = add_date_to_dic(y, today_date)
    # print(yy)
    create_or_append_csv_df_stock(current_zip_code, yy, today_date)

    create_or_append_csv_df(current_zip_code,xx,today_date))
