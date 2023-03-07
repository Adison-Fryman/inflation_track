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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(greeting)

    #each instance of Parse_and_save is stored in the parse_instances dictionary with a unique key based on the location and date.
    parse_instances = {}

    for location in locations_dict:
            instance_key = f'{location}.{today_date}'
            parse_instance = parse.Parse_and_save(location)
            # entry point of request string, creates the text file, then closes it
            parse_instance.create_txt_files()
            # Create variables raw_string, raw_items, names, prices, stock and zip dictionaries from txt file.
            # as well as final dated dictionaries ready for DF's
            parse_instance.run_parse_machine()
            #creates or appends DF's
            parse_instance.create_add_df()
            #saves instance to dictionary incase I need to access information later.
            parse_instances[instance_key] = parse_instance


    print('you are all done, check the files and DFs')
    #print('please check that your data frames look correct, before uploading data to dashboard')
