import unittest
import os
from item_price_parse import Parse_and_save
import datetime
from datetime import timedelta
date1 = datetime.date.today()
today_date = date1.strftime("%Y%m%d")
import tempfile

class TestParseAndSave(unittest.TestCase):
    def setUp(self):
        # Set up the test by creating an instance of the Parse_and_save class
        self.location = "test_location"
        self.test_date = today_date
        self.parser = Parse_and_save(self.location)
        self.file_path = fr'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.location}.txt'
        #self.file_path = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date.replace('/', '\\')}.{self.location}.txt'''
        #self.file_path = fr'''C:\\dev\\inflation_track\\walmart_cart_date.location.price\\{self.test_date.replace('/', '\\')}.{self.location}.txt'''
    def tearDown(self):
        # Clean up the test by deleting the test file if it was created
        txt_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.location}.txt'
        txt_file_path_multiple = f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.location}_multiple.txt'
        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
        if os.path.exists(txt_file_path_multiple):
            os.remove(txt_file_path_multiple)


    def test_create_txt_files(self):
        # Test that the function creates a new text file if one does not already exist
        self.parser.create_txt_files()
        txt_file_path = f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.location}.txt'
        self.assertTrue(os.path.exists(txt_file_path))

        # Test that the function does not overwrite an existing text file and instead creates a new file with a _multiple suffix
        self.parser.create_txt_files()
        txt_file_path_multiple = f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.location}_multiple.txt'
        print()
        self.assertTrue(os.path.exists(txt_file_path_multiple))

    def test_parse_walmart_request(self):
        # create a temporary file and write some data to it
        #request_string = 'Test data'
        with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\{today_date}.{self.location}.txt',
                  'w') as new_file_name:
            print('Test data', file=new_file_name)

            # instantiate a Parse_and_save object
            parser = Parse_and_save(self.location)

            # call the parse_walmart_request method
            parser.parse_walmart_request()
            print(parser.base_string)
            # assert that the base_string attribute on the object is equal to the data in the temporary file
            expected_data = 'Test data'
            self.assertEqual(parser.base_string, expected_data)
            print(parser.base_string,'Test data')





        #class TestParseWalmartRequest(unittest.TestCase):


   # def setUp(self):
     #   self.test_location = '49548'
      #  self.test_date = '20230320'
      #  self.file_path = fr'''C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.test_location}.txt'''








      #  f = open(self.file_path, "r")
     #   base_string = f.read()
      #  f.close()
     #   #logging.info('base string made')- do people make logging for testing
      #  self.base_string = base_string

   # def test_create_txt_files(self):
      #  #make sure the file gets created
      #  with open(f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.test_location}_unittest.txt',
       #           'w') as new_file_name:
       #     print(self.request_string, file=new_file_name)
      #  test_file_name = f'C:\dev\inflation_track\walmart_cart_date.location.price\{self.test_date}.{self.test_location}_unittest.txt'
      #  if os.path.exists(test_file_name):
       #     result = True
      #  else:
      #      result = False

      #  self.assertEqual(result,True)
        #make sure file can be detected that the file is where it should be.

    #def test_parse_walmart_request(self):
      #  with open(self.file_path, "w") as f:
       #     f.write(self.base_string)
      #  result = parse_walmart_request(self.file_path)
      #  self.assertEqual(result, ["", '{"itemPrice":{"$3.99"},"name":"Apple"},{"itemPrice":{"$2.99"},"name":"Banana"},{"itemPrice":{"$1.99"},"name":"Carrot"}]'])

   # def test_raw_items_strings(self):
      #  result = raw_items_strings(['',"{'itemPrice':{'$3.99'},'name':'Apple'},{'itemPrice':{'$2.99'},'name':'Banana'},{'itemPrice':{'$1.99'},'name':'Carrot'}"])
      #  self.assertEqual(result, ["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])

  #  def test_get_items_prices(self):
       # result = get_items_prices(["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
       # self.assertEqual(result, ['3.99', '2.99', '1.99'])

   # def test_get_item_names(self):
      #  result = get_item_names(["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
       # self.assertEqual(result, ['Apple', 'Banana', 'Carrot'])

   # def test_get_stock_availability(self):
       # result = get_stock_availability(["{'itemPrice':{'$3.99'},'name':'Apple','availabilityStatus':'OUT_OF_STOCK'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
      #  self.assertEqual(result, ['NO', 'yes', 'yes'])
