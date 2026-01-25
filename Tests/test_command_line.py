'''
Test command line file
'''

import unittest
from command_line import * #note, specify this late

class CountryTests(unittest.TestCase):
    def setUp(self):
        main()

    def test_per_capita_valid(self):
        '''Test valid country and year inputs'''
        result = get_per_capita_water_use("Japan", "2018")
        self.assertAlmostEqual(result, 290.58, places=2)

    def test_per_capita_invalid_country(self):
        '''Test invalid country input'''
        with self.assertRaises(ValueError):
            get_per_capita_water_use("Wakanda", "2018")

    def test_per_capita_invalid_year(self):
        with self.assertRaises(ValueError):
            get_per_capita_water_use("Japan", "1000")
    
    
    

