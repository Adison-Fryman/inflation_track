#location dictionary for manual requests
locations_dict = { '49548': "355 54th St SW, Wyoming, MI 49548",
 '72758': "4208 Pleasant Crossing Blvd, Rogers, AR 72758 --Rogers Supercenter4208",
 '33607': "1505 N Dale Mabry Hwy, Tampa, FL 33607 --Tampa Supercenter",
 '19137': "2200 Wheatsheaf Ln, Philadelphia, PA 19137 --Philadelphia Supercenter no num?",
 '93230': "250 S 12th Ave, Hanford, CA 93230 --Hanford Supercenter",
 '98057': "743 Rainier Ave S, Renton, WA 98057--Renton Supercenter",
 '58203': "5755 Gateway Dr, Grand Forks, ND 58203 --Grand Forks Supercenter",
              }


# this file will change the geographical locations in preparation for collecting the item prices at each location.

# NOTE: (1/15/2023) reducing number of locations until automation of data collection is functioning.



# how long does it take to collect this by hand using requests? 15 -20 min
# ________instructions to collect data manually _______
#
# change zip, enter cart, inspect page, click network in (), refresh page,
# sort by type, scroll to "fetch" current name starts with eb54d8(dee44), size should be about 12.8 kb, click on the name,
# dictionary should start with : ({"data":{"cart":{"id":"),
# hit ctrl +shift+end, then copy.
# saving as date.zip in dev>project folder as .txt file

# locations Chosen:
# Address: 355 54th St SW, Wyoming, MI 49548
# Address: 4208 Pleasant Crossing Blvd, Rogers, AR 72758 --Rogers Supercenter4208
# Address: 1505 N Dale Mabry Hwy, Tampa, FL 33607 --Tampa Supercenter
# Address: 2200 Wheatsheaf Ln, Philadelphia, PA 19137 --Philadelphia Supercenter no num?
# Address: 250 S 12th Ave, Hanford, CA 93230 --Hanford Supercenter
# Address: 743 Rainier Ave S, Renton, WA 98057--Renton Supercenter
# Address: 5755 Gateway Dr, Grand Forks, ND 58203 --Grand Forks Supercenter

#Locations: removed at this time
# Address: 965 Broadhollow Rd, Farmingdale, NY 11735
# Address: 29574 W Seven Mile Rd, Livonia, MI 48152
# Address: 3302 SE Military Dr, San Antonio, TX 78223
# Address: 4001 Behrman Pl, New Orleans, LA 70114
# Address: 2545 Rimrock Ave, Grand Junction, CO 81505
# Address: 4505 W Charleston Blvd, Las Vegas, NV 89102
# Address: 5755 Gateway Dr, Grand Forks, ND 58203
# Address: 743 Rainier Ave S, Renton, WA 98057
# Address: 250 S 12th Ave, Hanford, CA 93230
