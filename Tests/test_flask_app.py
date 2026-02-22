"""Tests flask app file"""

import unittest
from unittest.mock import patch, MagicMock

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
    """Tests for the flask app."""
    def test_home(self):
        """Tests Homepage works"""
        result = home()
        self.assertIn("Global Water Usage Analysis API", result)

    def test_404(self):
        """Tests 404 error works"""
        result = page_not_found("")
        self.assertIn("404 - Page Not Found", result)

    @patch("ProductionCode.usage_proportion.DataSource")
    def test_proportion_flask_right(self,mock_datasource):
        """Tests the intended Flask outcome for usage proportion"""
        mock_datasource = MagicMock()
        mock_datasource.select_usage_percentage.return_value = 20 #number does not matter.
        result = usage_proportion_route("Argentina", "2023")
        self.assertIn("Water usage in Argentina in 2023",result)

    @patch("ProductionCode.per_capita.DataSource")
    def test_per_capita_right(self,mock_datasource):
        """Tests the intended Flask outcome for per capita function"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.select_per_capita.return_value = 265.32
        result = per_capita_route("Argentina", "2023")
        self.assertEqual(
            result, "Argentina's Water Usage per Capita: 265.32 Liters per day"
        )

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_water_usage_right(self,mock_datasource):
        """Tests the intended Flask outcome for water usage difference"""
        mock_datasource = MagicMock()
        mock_datasource.select_total_resources.return_value = 20 #number does not matter.
        result = water_use_route("usa", "2018", "2020")
        self.assertIn("Water usage in United States of America", result)
    @patch("ProductionCode.use_time_compare.DataSource")
    def test_water_usage_albania(self,mock_datasource):
        """Tests water usage for Albania"""
        mock_datasource = MagicMock()
        mock_datasource.select_total_resources.return_value = 20 #number does not matter.
        result = water_use_route("Albania", "2018", "2020")
        self.assertIn("Water usage in Albania", result)


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
        self.assertIn("The requested URL was not found on the server", str(response.data))

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_flask_app_water_use_us(self,mock_datasource):
        """Water use test for US"""
        mock_datasource = MagicMock()
        mock_datasource.select_total_resources.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/water_use/US/2003/2004/")
        self.assertIn(
            "Water usage in United States of America\\n2003", str(response.data)
        )
    @patch("ProductionCode.usage_proportion.DataSource")
    def test_flask_app_usage_proportion(self,mock_datasource):
        """Usage proportion test via API"""
        mock_datasource = MagicMock()
        mock_datasource.select_usage_percentage.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/usage_proportion/Argentina/2023/")
        self.assertIn("Water usage in Argentina", str(response.data))
