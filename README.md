
Inflation_Track

Project to collect data on grocery costs and stock availability across multiple Walmart locations in the United States. 


Description: This project runs from main.py, it will supply the zip code to be entered into the site and then wait for the request string to be input into the Python Console/Terminal within the IDE. It will check various qualifications for the string, and while logging also output quick notes to the user about the quality of the data and any known issues. It will then tell you when it is complete and provide the next zip code. The locations are on a loop and when all locations have a provided string the program ends. 

Installation: (dependencies or requirements) Currently this needs to be run in and IDE. The string is far to long to put into the console.

Usage: 

1. Change zip, select locations.
2. Navigate to cart
3. Inspect page, 
4. Click "network" in Developer Console, 
5. Refresh page,
6. Sort by type, scroll to "fetch" current name starts with eb54d8(dee44) changes daily, size should be about 12.8+ kb, 
7. Click on the name, dictionary should start with : "({"data":{"cart":{"id":")"
8. Hit ctrl +shift+end, then ctrl + c
9. Paste into Python Console/Terminal

Configuration: None Currently 

Contributing: Guidelines for contributing to the project- Please do not.

License: NA


Roadmap for future development: I would like to automate this as much as possible, get a GUI set up so it is not in the IDE. The reality is that Walmart does not want bots on their webpage, so I have been using manual manipulation to navigate the webpage. There are some possible options with requests and API's, but at this time I am going to go forward with the data visualization and live dashboard creation. The program is working fine as it is and the data acquisition takes me about 10 minutes once a week. If I do find an efficient method of automation that does not break any laws or infringe on Walmart’s rights, I would like to add more locations and not just food but other necessities. 

Current list of locations:
# Address: 355 54th St SW, Wyoming, MI 49548
# Address: 4208 Pleasant Crossing Blvd, Rogers, AR 72758 --Rogers Supercenter4208
# Address: 1505 N Dale Mabry Hwy, Tampa, FL 33607 --Tampa Supercenter
# Address: 2200 Wheatsheaf Ln, Philadelphia, PA 19137 --Philadelphia Supercenter no num?
# Address: 250 S 12th Ave, Hanford, CA 93230 --Hanford Supercenter
# Address: 743 Rainier Ave S, Renton, WA 98057--Renton Supercenter
# Address: 5755 Gateway Dr, Grand Forks, ND 58203 --Grand Forks Supercenter

Current list of items: 
# The intent is for it to be necessary caloric items. Traditional junk foods have not been added intentionally.
food_list = {'Bread':'Great Value 100% Whole Wheat Round Top Bread Loaf, 20 oz',
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
             'Can Tomatoes': 'Great Value Diced Tomatoes In Tomato Juice, 14.5 Oz'}

