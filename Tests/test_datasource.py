"""
Test command line file
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock

from ProductionCode.database import DataSource



class TestDataSource(unittest.TestCase):
    """Tests basic datasource functions"""

    @patch("ProductionCode.database.records.Database")
    def test_run_string_psql(self, mock_db_class):
        """Tests runstring PSQL!"""
        mock_db_instance = mock_db_class.return_value


        mock_return = MagicMock()
        
        mock_return.all.return_value = [{"total_resources": 13}]


        mock_return.__getitem__.return_value = [{"total_resources": 13}]
        mock_db_instance.query.return_value = mock_return



        ds = DataSource()
        result = ds.run_string_psql("this isn't a real SQL command")
        
        self.assertEqual(13, result[0]["total_resources"])

    @patch("ProductionCode.database.records.Database")
    def test_run_string_psql_multiple(self, mock_db_class):
        """Tests runstring PSQL multiple"""
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.query.return_value = [{"total_resources": 13}]
        ds = DataSource()
        result = ds.run_string_psql_multiple("this isn't a real SQL command")[0]
        self.assertEqual(13, result["total_resources"])

    @patch("ProductionCode.database.records.Database")
    def test_get_countries(self,mock_db_class):
        """Tests the get countries function."""
        mock_db_instance = mock_db_class.return_value
        
        mock_row = MagicMock()

        mock_row.country = "FAKE COUNTRY"

        mock_db_instance.query.return_value = [mock_row]
        ds = DataSource()
        self.assertIn("FAKE COUNTRY",ds.get_countries("fake_data_set"))

    @patch("ProductionCode.database.records.Database")
    def test_get_usage_percentage(self,mock_db_class):
        """Tests the get_usage_percentage function."""
        mock_db_class.return_value = "this is pointless"
        mock_return = MagicMock()

        mock_function = MagicMock(name="run_string_psql")
        mock_return.agriculture_total = [1337]
        mock_return.industrial_total = [420]
        mock_return.household_total = [67]
        
        mock_function.return_value = mock_return

        ds = DataSource()

        ds.run_string_psql = mock_function
        self.assertIn(1337,ds.get_usage_percentage("UK",2001,0))
        self.assertIn(420,ds.get_usage_percentage("USA",2001,1))
        self.assertIn(67,ds.get_usage_percentage("USA",2001,2))