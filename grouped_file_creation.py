import csv
import pandas as pd
from Location_Change import locations
from list_of_items import food_list
from item_price import df_holding

### do not ever use this!!!! I have added "_a" so the files with all the data can not be over written. This is for records only.
def create_txt_files():
    for location in locations:
        with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{location}_a.txt',
                  'w') as new_file_name:
            print("item", file=new_file_name)
            for food_item in food_list:
                print(food_item, file=new_file_name)



def create_csv_files():
    for location in locations:
        headers = food_list = {'Bread':'Great Value 100% Whole Wheat Round Top Bread Loaf, 20 oz',
             'Peanut Butter (Jif)':'Jif Creamy Peanut Butter, 16-Ounce Jar',
             'Cheese':'Great Value Sharp Cheddar Cheese, 16 oz',
             'Eggs':'Great Value Large White Eggs, 18 Count',
             'Milk':'Great Value Whole Vitamin D Milk, Gallon, 128 fl oz',
             'Turkey':'Great Value Thin Sliced Oven Roasted Turkey Breast Family Pack, 8 oz, 2 Ct',
             'Celery':'Celery Stalk',
             'Carrots':'Whole Carrots, 16 Oz bag',
             'Fresh Tomato':'Fresh Roma Tomato, Each',
             'Orange':'Navel Oranges',
             'Apples': 'Freshness Guaranteed Granny Smith Apples, 3 lb Bag',
             'Frozen Chicken':'Great Value Boneless Skinless Chicken Breast, 3 lb (Frozen)',
             'Frozen Beef':'Great Value Beef Burgers, 75% Lean/25% Fat, 12 Count, 3 lbs (Frozen)',
             'Frozen Peas':'Great Value Frozen Sweet Peas, 32 oz Steamable Bag',
             'Olive Oil':'Great Value: 100% Extra Virgin Olive Oil, 25.5 fl oz',
             'Rice':'Great Value Long Grain Enriched Rice, 32 oz',
             'Black Beans': 'Great Value Black Beans, 15 oz Can',
             'Corn': 'Great Value Whole Kernel Corn, Canned Vegetables, 14.5-15 oz',
             'Peanut Butter (Great Value)': 'Great Value Creamy Peanut Butter, 18 oz Jar',
             'Can Tomatoes': 'Great Value Diced Tomatoes In Tomato Juice, 14.5 Oz'

             }
        for food_item in food_list:
            headers.append(food_item)

    data=pd.DataFrame(headers)
    print(data)






#create_csv_files()


add_date = {'date':'01232023'}
add_date.update(df_holding)
df = pd.DataFrame(add_date,index=[0])
df.to_csv(r'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\test.csv''')
# use df_holding to make dataframe headers and first row, then add next row. I do not know if I can create csv files from here or just save to them.

