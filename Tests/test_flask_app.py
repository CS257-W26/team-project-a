"""Tests flask app file"""

import unittest
from unittest.mock import patch, MagicMock

from flask_app import (
    water_use_route,
    usage_proportion_route,
    per_capita_route,
    app,
    api,
)


class FlaskTest(unittest.TestCase):
    """Tests for the flask app."""

    @patch("ProductionCode.usage_proportion.DataSource")
    def test_proportion_flask_right(self,mock_datasource):
        """Tests the intended Flask outcome for usage proportion"""
        mock_datasource = MagicMock()
        mock_datasource.get_usage_percentage.return_value = 20 #number does not matter.
        result = usage_proportion_route("Argentina", "2023")
        self.assertIn("Water usage in Argentina in 2023",result)

    @patch("ProductionCode.per_capita.DataSource")
    def test_per_capita_right(self,mock_datasource):
        """Tests the intended Flask outcome for per capita function"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_per_capita.return_value = 265.32
        result = per_capita_route("Argentina", "2023")
        self.assertEqual(
            result, "Argentina's Water Usage per Capita: 265.32 Liters per day"
        )

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_water_usage_right(self,mock_datasource):
        """Tests the intended Flask outcome for water usage difference"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_total_resources.return_value = 20 #number does not matter.
        result = water_use_route("usa", "2018", "2020")
        self.assertIn("20", result)
    @patch("ProductionCode.use_time_compare.DataSource")
    def test_water_usage_albania(self,mock_datasource):
        """Tests water usage for Albania"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_total_resources.return_value = 20 #number does not matter.
        result = water_use_route("Albania", "2018", "2020")
        self.assertIn("20", result)


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
        self.assertIn("Water Usage Statistics", str(response.data))

    def test_flask_app_404(self):
        """404 test for flask"""
        response = self.run_test_site("/WEWLAD/")
        self.assertIn("Page Not Found", str(response.data))

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_flask_app_water_use_us(self,mock_datasource):
        """Water use test for US"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_total_resources.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/water_use/US/2003/2004/")
        self.assertIn(
            "20", str(response.data)
        )
    @patch("ProductionCode.usage_proportion.DataSource")
    def test_flask_app_usage_proportion(self,mock_datasource):
        """Usage proportion test via API"""
        mock_datasource = MagicMock()
        mock_datasource.get_usage_percentage.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/usage_proportion/Argentina/2023/")
        self.assertIn("Water usage in Argentina", str(response.data))

    @patch("ProductionCode.per_capita.DataSource")
    def test_flask_app_per_capita(self,mock_datasource):
        """Per captia test via API"""
        mock_datasource = MagicMock()
        mock_datasource.get_usage_percentage.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/per_capita/Argentina/2023/")
        self.assertIn("1.0 Liters per day", str(response.data))

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_flask_app_compare(self,mock_datasource):
        """Compare test via API"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_total_resources.return_value = 20 #number does not matter.
        response = self.run_test_site("/api/water_use/Argentina/2023/2021")
        self.assertIn("20", str(response.data))


class TestHtmlApp(unittest.TestCase):
    """Integration tests for frontend"""
    def setUp(self):
        if "api" not in app.blueprints:
            app.register_blueprint(api, url_prefix="/api")

    def run_test_site(self,url,post_data):
        """Helper function to quickly run the test flask site."""
        cur_app = app.test_client()
        return cur_app.post(url,data=post_data)

    @patch("flask_app.get_per_capita_water_use")
    @patch("flask_app.get_usage_proportion")
    @patch("flask_app.get_countries")
    def test_flask_app_per_capita(self,mock_get_countries,
                                  mock_get_usage_proportion,mock_get_per_capita):
        """Per captia test. Very scuffed. IDK how to do this better."""
        mock_get_countries.return_value = ["Australia"]
        mock_get_usage_proportion.return_value = {
            "Agricultural": 20,
            "Industrial": 20,
            "Household": 20,
        }
        mock_get_per_capita.return_value = 42069.0
        response = self.run_test_site("/usage",{
            "country": "Australia",
            "year": "2005",
        })
        self.assertIn("42069.0 Liters per day", str(response.data))

    @patch("flask_app.get_usage_proportion")
    @patch("flask_app.get_countries")
    def test_flask_app_per_capita_invalid(self,mock_get_countries,mock_get_usage_proportion):
        """Per captia test for invalid country/year"""
        mock_get_countries.return_value = ["Australia"]
        mock_get_usage_proportion.side_effect = ValueError()
        response = self.run_test_site("/usage",{
            "country": "Australia",
            "year": "2005",
        })
        self.assertIn("Invalid", str(response.data))

    @patch("flask_app.get_per_capita_water_use")
    @patch("flask_app.get_usage_proportion")
    @patch("flask_app.get_countries")
    def test_flask_app_proportion(self,mock_get_countries,
                                  mock_get_usage_proportion,mock_get_per_capita):
        """This test does not work properly?? I'm not sure how to fix it. Lol.
        Should test weather the proportions work.
        """
        mock_get_countries.return_value = ["Australia"]
        mock_get_usage_proportion.return_value = {
            "Agricultural": 20,
            "Industrial": 20,
            "Household": 20,
        }
        mock_get_per_capita.return_value = 42069
        response = self.run_test_site("/usage",{
            "country": "Australia",
            "year": "2005",
        })
        self.assertIn("Australia", str(response.data))

    @patch("flask_app.get_usage_proportion")
    @patch("flask_app.get_countries")
    def test_flask_app_proportion_invalid(self,mock_get_countries,mock_get_usage_proportion):
        """Tests an invalid country/year for proprotion.
        """
        mock_get_countries.return_value = ["Australia"]
        mock_get_usage_proportion.side_effect = ValueError()
        response = self.run_test_site("/usage",{
            "country": "AAA",
            "year": "2005",
        })
        self.assertIn("Invalid", str(response.data))


    @patch("flask_app.water_use_time_compare")
    @patch("flask_app.get_compare_countries")
    def test_flask_app_compare(self,mock_get_compare_countries,mock_water_use_time_compare):
        """Usage compare. Very scuffed. IDK how to do this better.
        HELP ME
        """
        mock_get_compare_countries.return_value = ["Albania"]
        mock_water_use_time_compare.return_value = ["Albania", "2004", "2005", "20", "20"]

        response = self.run_test_site("/compare",{
            "country": "Albania",
            "year1": "2004",
            "year2": "2005",
        })
        self.assertIn("20.0 US$/m^3", str(response.data))

    @patch("flask_app.water_use_time_compare")
    @patch("flask_app.get_compare_countries")
    def test_flask_app_compare_failure(self,mock_get_compare_countries,mock_water_use_time_compare):
        """Usage compare test for a nonexistant country."""
        mock_get_compare_countries.return_value = ["Albania"]
        mock_water_use_time_compare.side_effect = ValueError()

        response = self.run_test_site("/compare",{
            "country": "HELL",
            "year1": "2004",
            "year2": "2005",
        })
        self.assertIn("Invalid", str(response.data))
