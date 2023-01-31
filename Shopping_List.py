
#****temp holding place for quick in project tests
# this file will add the shopping list item by item.

import re
import pandas as pd
from Location_Change import locations

import os.path
#print(os.path.exists('C:\\'))

from list_of_items import food_list

name_price ={'Celery Stalk': '$1.74 ',
             'Whole Carrots, 16 Oz bag': '$0.98 ',
             'Great Value Boneless Skinless Chicken Breast, 3 lb (Frozen)': '$9.74 ',
             'Great Value Beef Burgers, 75% Lean/25% Fat, 12 Count, 3 lbs (Frozen)': '$11.82 ',
             'Great Value: 100% Extra Virgin Olive Oil, 25.5 fl oz': '$5.50 ',
             'Great Value 100% Whole Wheat Round Top Bread Loaf, 20 oz': '$1.88 ',
             'Great Value Long Grain Enriched Rice, 32 oz': '$1.62 ',
             'Great Value Black Beans, 15 oz Can': '$0.78 ',
             'Great Value Golden Sweet Whole Kernel Corn, 15 oz': '$0.58 ',
             'Great Value Frozen Sweet Peas, 32 oz Steamable Bag': '$2.28 ',
             'Jif Creamy Peanut Butter, 16-Ounce Jar': '$2.76 ',
             'Great Value Creamy Peanut Butter, 18 oz Jar': '$1.84 ',
             'Great Value Diced Tomatoes in Tomato Juice, 14.5 oz Can': '$0.88 ',
             'Fresh Roma Tomato, Each': '$0.44 ',
             'Navel Oranges': '$0.88 ',
             'Freshness Guaranteed Granny Smith Apples, 3 lb Bag': '$5.98 ',
             'Great Value Thin Sliced Oven Roasted Turkey Breast Family Pack, 8 oz, 2 Ct': '$6.72 ',
             'Great Value Sharp Cheddar Cheese, 16 oz': '$3.68 ',
             'Great Value Large White Eggs, 18 Count': '$7.07 ',
             'Great Value Whole Vitamin D Milk, Gallon, 128 fl oz': '$2.78 '}


final_data_sorted_named_clean = {}
for food_item, description in food_list.items():
        #locates the most important word of the food description
    food_item_words = food_item.lower().split()
    food_item_last_word=food_item_words[-1]

    if description in name_price:
        final_data_sorted_named_clean[food_item] = name_price[description]
    else:
        final_data_sorted_named_clean[food_item] = 'item not found'
        print('not found:' + food_item)
        print(food_item_last_word)
        print()


print(final_data_sorted_named_clean)




















#data_in_directory = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\19137.csv'''
#file_location = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped'''

#print(os.path.exists("walmart_cart_date.location.price\grouped"))
#print(os.listdir("walmart_cart_date.location.price\grouped"))


#print(os.path.exists(data_in_directory))
#print(os.listdir(file_location))

#for location in locations:
    #print( os.path.exists(fr'''C:\dev\inflation_track\walmart_cart_date.location.price\grouped\{location}.csv'''))
