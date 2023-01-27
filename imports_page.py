# print(f.read())
# *****temp holding place for parsing the number of items.
base_string = f.read()
# print(base_string)
base = base_string.split('"lineItems":[{"')

# getting '"switchableQuantity"
# this is to check items are all instock

quant2 = base[0]
import re

#f = open(r"C:\dev\inflation_track\walmart_cart_date.location.price\01232023.19137.txt", "r")

x = [m.start() for m in re.finditer('"switchableQuantity":', quant2)]
a, b, c = x[0], x[1], x[2]
# print(len('"switchableQuantity":21,'))
switchableQuantity = quant2[a:a + 24], quant2[b:b + 24], quant2[c:c + 24]
# print(switchableQuantity)

# also look for totalItemQuantity, to help determine if items are missing?

# use .pop to remove first or last item?
items = str(base[1])
by_item1 = items.split('"itemPrice":{"')
by_item2 = by_item1[1:]
# print(len(by_item2))
# print(by_item2[0])
# print(by_item2[-1])