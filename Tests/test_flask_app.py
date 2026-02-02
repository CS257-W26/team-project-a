"""Tests flask app file"""

import unittest
from flask_app import (
    home,
    water_use_route,
    usage_proportion_route,
    per_capita_route,
    page_not_found,
    app,
    api,
)


class FlaskTest(unittest.TestCase):

    def test_home(self):
        """Tests Homepage works"""
        result = home()
        self.assertEqual(
            result, "Welcome to the Global Water Sources v Spending website!"
        )

    def test_404(self):
        """Tests 404 error works"""
        result = page_not_found("")
        self.assertEqual(result, "Page not found. Try re-entering the link. Error: ")

    def test_proportion_flask_right(self):
        """Tests the intended Flask outcome for usage proportion"""
        result = usage_proportion_route("Argentina", "2023")
        self.assertEqual(
            result,
            "Water usage in Argentina in 2023\nAgricultural:40.84%\nIndustrial:26.1%\nHousehold:29.27%\n",
        )

    def test_per_capita_right(self):
        """Tests the intended Flask outcome for per capita function"""
        result = per_capita_route("Argentina", "2023")
        self.assertEqual(
            result, "Argentina's Water Usage per Capita: 265.32 Liters per day"
        )

    def test_water_usage_right(self):
        """Tests the intended Flask outcome for water usage difference"""
        result = water_use_route("usa", "2018", "2020")
        self.assertEqual(
            result,
            "Water usage in United States of America\n2018: 1829x10^9 cubic meters/year\n2020: 1829x10^9 cubic meters/year\nDifference:\n0x10^9 cubic meters/year",
        )


class TestFlaskApp(unittest.TestCase):
    """Tests for le flask app internal functionality."""

    def setUp(self):
        if "api" not in app.blueprints:
            app.register_blueprint(api, url_prefix="/api")

    def run_test_site(self, url="/"):
        """Helper function to quickly run the test flask site."""
        cur_app = app.test_client()
        return cur_app.get(url, follow_redirects=True)

    def test_flask_app_homepage(self):
        """Homepage test for flask"""
        response = self.run_test_site("/")
        self.assertIn("Welcome to the Global Water", str(response.data))

    def test_flask_app_404(self):
        """404 test for flask"""
        response = self.run_test_site("/WEWLAD/")
        self.assertIn("Page not found. Try re-entering the link. Error", str(response.data))

    def test_flask_app_water_use(self):
        """Homepage test for flask"""
        response = self.run_test_site("/water_use/US/2003/2004")
        self.assertIn(
            "Water usage in United States of America\\n2003", str(response.data)
        )

    def test_get_row(self):
        """Tests basic API function."""
        response = self.run_test_site("/api/1/1/")
        self.assertIn("30.613806827", str(response.data))

    def test_get_row_col_invalid_row(self):
        """Tests API error handling for nonexistant DB"""
        response = self.run_test_site("/api/100000000/1")
        self.assertIn("Could not find the requested", str(response.data))

    def test_get_row_col_invalid_col(self):
        """Tests API error handling for nonexistant row"""
        response = self.run_test_site("/api/1/10000000000")
        self.assertIn("Could not find the requested", str(response.data))
