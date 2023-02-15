class TestParseWalmartRequest(unittest.TestCase):
    def setUp(self):
        self.file_path = "sample_file.txt"
        self.base_string = "lineItems":[{"itemPrice":{"$3.99"},"name":"Apple"},{"itemPrice":{"$2.99"},"name":"Banana"},{"itemPrice":{"$1.99"},"name":"Carrot"}]"

    def test_parse_walmart_request(self):
        with open(self.file_path, "w") as f:
            f.write(self.base_string)
        result = parse_walmart_request(self.file_path)
        self.assertEqual(result, ["", '{"itemPrice":{"$3.99"},"name":"Apple"},{"itemPrice":{"$2.99"},"name":"Banana"},{"itemPrice":{"$1.99"},"name":"Carrot"}]'])

    def test_raw_items_strings(self):
        result = raw_items_strings(['',"{'itemPrice':{'$3.99'},'name':'Apple'},{'itemPrice':{'$2.99'},'name':'Banana'},{'itemPrice':{'$1.99'},'name':'Carrot'}"])
        self.assertEqual(result, ["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])

    def test_get_items_prices(self):
        result = get_items_prices(["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
        self.assertEqual(result, ['3.99', '2.99', '1.99'])

    def test_get_item_names(self):
        result = get_item_names(["{'itemPrice':{'$3.99'},'name':'Apple'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
        self.assertEqual(result, ['Apple', 'Banana', 'Carrot'])

    def test_get_stock_availability(self):
        result = get_stock_availability(["{'itemPrice':{'$3.99'},'name':'Apple','availabilityStatus':'OUT_OF_STOCK'}", "{'itemPrice':{'$2.99'},'name':'Banana'}", "{'itemPrice':{'$1.99'},'name':'Carrot'}"])
        self.assertEqual(result, ['NO', 'yes', 'yes'])
