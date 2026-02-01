'''Tests flask app file'''

import unittest
from flask_app import home, water_use_route, usage_proportion_route, per_capita_route, page_not_found


class FlaskTest(unittest.TestCase):

    def test_home(self):
        """Tests Homepage works"""
        result = home()
        self.assertEqual(result,"Welcome to the Global Water Sources v Spending website!")

    def test_404(self):
        """Tests 404 error works"""
        result = page_not_found("Argentina")
        self.assertEqual(result,("Page not found", 404))

    def test_proportion_flask_right(self):
        """Tests the intended Flask outcome for usage proportion"""
        result = usage_proportion_route("Argentina", "2023")
        self.assertEqual(result,
            "Water usage in Argentina in 2023\nAgricultural:40.84%\nIndustrial:26.1%\nHousehold:29.27%\n")
    
    def test_per_capita_right(self):
        """Tests the intended Flask outcome for per capita function"""
        result = per_capita_route("Argentina", "2023")
        self.assertEqual(result,
            "Argentina's Water Usage per Capita: 265.32 Liters per day")
    
    def test_water_usage_right(self):
        """Tests the intended Flask outcome for water usage difference"""
        result = water_use_route("usa", "2018", "2020")
        self.assertEqual(result,
            "Water usage in United States of America\n2018: 1829x10^9 cubic meters/year\n2020: 1829x10^9 cubic meters/year\nDifference:\n0x10^9 cubic meters/year")
