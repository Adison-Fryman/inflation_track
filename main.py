
# project will collect data from walmart site, cost of a shopping cart by item for grocery pick up from locations
# across the United States.


# collect data daily for 1 week to get enough to  accurately create database in SQL.

#Current todo
# set up function run in main from item_price to create first set of CSV files with the first two sets of parsed and cleaned data.
import datetime
from Location_Change import locations

print('''Hello, are you logged in to the walmart site...
        https://www.walmart.com/cart 
 
        and inside your cart for the first location? 
 
        first Location:    49548    
        
        ''')

date1 = datetime.date.today()
date= date1.strftime("%m%d%Y")

for location in locations:
    print("Location:"+ location)
    request=input(fr"When ready put the network request for {location} here as a string :")
    # save it as a txt file with this format:
    #get location of text file
        # should look like this V = r'''C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt'''
    # run V through parse_walmart_request
    #check that it looks ok? optional second rev
    # run through add_date_to_item_price_dic(items_prices={}, date=''):
    # run through create_or_append_csv_df(zip_code,date_added={}, date=''):
    #add location to matrix?


print('please check that your data frames look correct, before uploading data to dashboard')


