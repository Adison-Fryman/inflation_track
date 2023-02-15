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


def auto_bot():
    # save it as a txt file with this format:
    # get location of text file
    # should look like this V = r'''C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt'''
    # run text file through parse_walmart_request
    # check that it looks ok? optional second rev
    # run through add_date_to_item_price_dic(items_prices={}, date=''):
    # run through create_or_append_csv_df(zip_code,date_added={}, date=''):
    # add location to matrix?
    pass


def create_txt_files(location, date):
    #update this so that it does not overwrite files that already exist.
    request_string = input(fr"When ready put the network request for {location} here as a string :")
    with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\{date}.{location}.txt',
              'w') as new_file_name:
        print(request_string, file=new_file_name)

def continue_yes_no():
    #write a way out after an error
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(greeting)

    for location in locations_dict:
        create_txt_files(location, today_date)
        #check that old date format and new date format are correct everywhere
        text_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.price\{today_date}.{location}.txt'
        #remove the "_a " and "test" from file saving when ready
        raw_string = parse.parse_walmart_request(text_file_path)
        raw_items = (parse.raw_items_strings(parse.parse_walmart_request(text_file_path)))

        names = parse.get_item_names(raw_items)
        prices = parse.get_items_prices(raw_items)
        stock = parse.get_stock_availability(raw_items)

        name_stock = dict(zip(names, stock))
        name_price = dict(zip(names, prices))
        print(parse.get_num_items_from_string(raw_string))
        print(parse.get_num_items_from_stock_dict(name_stock))
        #check post code
        print(f'location in file: {parse.check_postal_code(location, raw_string)} location intended:{location}')
        #check date-whole date- only returns date string, need to ask user if date string is ok
        print(parse.check_date(raw_string))
        x = parse.ordered_food_price_dict(name_price)
        y = parse.add_date_to_item_price_dic(x,today_date)
        z = parse.create_or_append_csv_df(location,y,today_date)
        print(x)

    print('please check that your data frames look correct, before uploading data to dashboard')
