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
    def test_run_string_psql(self, mock_db_class): #DEPRECATED!
        """Tests runstring PSQL - DEPRECATED!"""
        mock_db_instance = mock_db_class.return_value

        mock_db_instance.query.return_value = {"total_resources": 13}
        ds = DataSource()
        result = ds.run_string_psql_multiple("this isn't a real SQL command")
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