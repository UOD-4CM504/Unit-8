import unittest
import json
import os
import copy
from Exercise_2 import save, load, add_item

class TestMenuOperations(unittest.TestCase):
    def setUp(self):
        # Define test data
        self.filename = "menu.json"
        self.test_menu = {"menu": {"1": {"Name": "Test Pizza", "Price": 11.99}}, "next_id": 2}

    def test_save_and_load(self):
        # Save the original content if the file exists
        original_content = None
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                original_content = json.load(f)

        # Test save
        save(self.filename, self.test_menu)
        self.assertTrue(os.path.exists(self.filename), msg=f"File {self.filename} not saved successfully...")

        with open(self.filename) as f:
            menu_dict_test = json.load(f)
        self.assertEqual(menu_dict_test, self.test_menu, msg="Menu data not saved correctly")

        # Test load
        loaded_menu = load(self.filename)
        self.assertEqual(loaded_menu, self.test_menu, msg="Loaded menu does not match saved menu")

        # Restore original content if it existed
        if original_content is not None:
            save(self.filename, original_content)

    def test_add_item(self):
        menu_copy = copy.deepcopy(self.test_menu)
        add_item(menu_copy, "Onion Soup", "3.99")

        expected_menu = copy.deepcopy(self.test_menu)
        expected_menu["menu"]["2"] = {"Name": "Onion Soup", "Price": 3.99}
        expected_menu["next_id"] = 3

        self.assertEqual(menu_copy, expected_menu, msg="Item not added correctly")

if __name__ == '__main__':
    unittest.main()