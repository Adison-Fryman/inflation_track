import item_price_parse as parse
from locations import locations_dict
import datetime

greeting = '''Hello, are you logged in to the walmart site...
        https://www.walmart.com/cart 

        and inside your cart for the first location? 

        first Location:    49548    

        '''

date1 = datetime.date.today()
today_date = date1.strftime("%Y%m%d")




def create_txt_files(location, date):
    #update this so that it does not overwrite files that already exist.
    request_string = input(fr"When ready put the network request for {location} here as a string :")
    with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\{date}.{location}.txt',
              'w') as new_file_name:
        print(request_string, file=new_file_name)


def auto_bot():
    for location in locations_dict:
        create_txt_files(location, today_date)
        text_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.price\{today_date}.{location}_a.txt'
        # remove the "_a " and "test" from file saving when ready
        raw_string = parse.parse_walmart_request(text_file_path)
        raw_items = (parse.raw_items_strings(parse.parse_walmart_request(text_file_path)))

        names = parse.get_item_names(raw_items)
        prices = parse.get_items_prices(raw_items)
        stock = parse.get_stock_availability(raw_items)

        name_stock = dict(zip(names, stock))
        name_price = dict(zip(names, prices))
        print(parse.get_num_items_from_stock_dict(name_stock))
        # check post code
        print(f'location in file: {parse.check_postal_code(location, raw_string)} location intended:{location}')
        # check date-whole date- only returns date string, need to ask user if date string is ok
        print(parse.check_date(raw_string))
        x = parse.ordered_food_price_dict(name_price)
        y = parse.add_date_to_dic(x, today_date)
        # i dont think I need to name this z
        z = parse.create_or_append_csv_df(location, y, today_date)
        print(x)
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(greeting)

    for location in locations_dict:
        # entry point of request string, creates the text file, then closes it. This is the "test" version to prevent over writing data in DF's.
        # Take request string, create txt file, close. Create variables raw_string and raw_items from txt file.
        create_txt_files(location, today_date)
        text_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.price\{today_date}.{location}.txt'
        raw_string = parse.parse_walmart_request(text_file_path)
        raw_items = (parse.raw_items_strings(parse.parse_walmart_request(text_file_path)))

        # check raw string for date, and zip code before creating dictionaries
        checking_postcode = parse.check_postal_code(location, raw_string)
        print(parse.postal_code_match(checking_postcode, location))
        print(parse.check_date(raw_string))

        # create clean list variables from raw_items
        names = parse.get_item_names(raw_items)
        prices = parse.get_items_prices(raw_items)
        stock = parse.get_stock_availability(raw_items)

        # create dictionary variables from the above list variables of names:prices and names:stock
        name_stock = dict(zip(names, stock))
        name_price = dict(zip(names, prices))


        #gets total number of items in stock, or with errors for logging/reporting
        print(parse.get_num_items_from_stock_dict(name_stock))

        # Puts the price dict in the correct order for the DF, adds the date and then appends it to the DF in CSV format.
        in_order_prices = parse.ordered_food_price_dict(name_price)
        ordered_and_dated_prices = parse.add_date_to_dic(in_order_prices, today_date)
        print(ordered_and_dated_prices)
        parse.create_or_append_csv_df(location, ordered_and_dated_prices, today_date)

        in_order_stock = parse.ordered_name_stock_dict(name_stock)
        ordered_and_dated_stock = parse.add_date_to_dic(in_order_stock, today_date)
        # print(ordered_and_dated_stock)
        parse.create_or_append_csv_df_stock(location, ordered_and_dated_stock, today_date)

    print('please check that your data frames look correct, before uploading data to dashboard')
