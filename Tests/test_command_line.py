"""
Test command line file
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch, MagicMock

from ProductionCode.per_capita import get_per_capita_water_use
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.utils import print_help_statement
from command_line import main


# Running the line above is giving me an error.



class CommandLineTest(unittest.TestCase):
    """Tests command line running"""

    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    def test_run(self):
        """Basic test run"""
        sys.argv = []
        printed_out = self._run_and_return_output()
        self.assertEqual(
            printed_out,
            print_help_statement().strip(),
        )

    def test_run_none(self):
        """Tests for output with no input."""
        sys.argv = ["command_line.py"]
        printed_out = self._run_and_return_output()
        self.assertIn("COMMANDS", printed_out)

    def test_run_help(self):
        """Tests for output with help input."""
        sys.argv = ["command_line.py", "-help"]
        printed_out = self._run_and_return_output()
        self.assertIn("COMMANDS", printed_out)

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_run_water_use_time_compare(self,mock_datasource):  # THIS IS AN ACCEPTANCE TEST FOR #3
        """Tests water use compare"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_total_resources.return_value = 20 #number does not matter.
        sys.argv = ["command_line.py", "-usageovertime", "USA", "2001", "2003"]
        printed_out = self._run_and_return_output()
        self.assertIn("Water usage in United States of America", printed_out)

    @patch("ProductionCode.use_time_compare.DataSource")
    def test_run_water_use_time_compare_fail(self,mock_datasource):
        """Tests invalid water use compare"""
        mock_datasource = MagicMock()
        mock_datasource.get_total_resources.return_value = 20 #number does not matter.
        sys.argv = ["command_line.py", "-usageovertime", "USA", "2001"]
        printed_out = self._run_and_return_output()
        self.assertEqual(printed_out, print_help_statement().strip())

    def test_run_water_use_time_compare_invalid_year(self):
        """Tests invalid water use compare with bad year"""
        sys.argv = [
            "command_line.py",
            "-usageovertime",
            "USA",
            "2001",
            "243243125245324",
        ]
        self.assertRaises(ValueError, self._run_and_return_output)

    @patch("ProductionCode.per_capita.DataSource")
    def test_per_capita_command(self,mock_datasource):  # THIS IS AN ACCEPTANCE TEST FOR #1
        """Test percapita command"""

        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_per_capita.return_value = 364.38
        # Do not ask me why this works. I have NO idea.
        sys.argv = ["command_line.py", "-percapita", "Argentina", "2024"]
        printed_out = self._run_and_return_output()
        self.assertIn(
            "364.38 Liters per day",
            printed_out,
        )


class PerCapitaWaterUseTest(unittest.TestCase):
    """Tests percapita water use"""

    @patch("ProductionCode.per_capita.DataSource")
    def test_per_capita_valid(self,mock_datasource):  # THIS IS AN ACCEPTANCE TEST FOR #2
        """Test valid country and year inputs"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_per_capita.return_value = 290.58
        result = get_per_capita_water_use("Japan", "2018")
        self.assertAlmostEqual(result, 290.58, places=2)

    @patch("ProductionCode.per_capita.DataSource")
    def test_per_capita_invalid_country(self,mock_datasource):
        """Test invalid country input"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_per_capita.return_value = None
        with self.assertRaises(IndexError):
            get_per_capita_water_use("Wakanda", "2018")

    def test_per_capita_invalid_year(self):
        """Test invalid year input"""
        with self.assertRaises(ValueError):
            get_per_capita_water_use("uk", "1000")


class UsageProportionTest(unittest.TestCase):
    """Tests usage proportions"""

    def _run_and_return_output(self) -> str:
        """Helper function thar runs the command line app and returns the output."""
        sys.stdout = StringIO()
        main()
        return sys.stdout.getvalue().strip()

    @patch("ProductionCode.usage_proportion.DataSource")
    def test_proportion_valid(self,mock_datasource):  # THIS IS AN ACCEPTANCE TEST FOR #1
        """Test valid country/year/type input"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_usage_percentage.return_value = 1337
        sys.argv = ["command_line.py", "-usageproportion", "Argentina", "2024"]
        printed_out = self._run_and_return_output()
        self.assertIn("1337", printed_out)

    @patch("ProductionCode.usage_proportion.DataSource")
    def test_proportion_invalid_country(self,mock_datasource):
        """Test invalid country input"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_usage_percentage.return_value = None
        with self.assertRaises(IndexError):
            usage_proportion("Wakanda", "2023")

    @patch("ProductionCode.usage_proportion.DataSource")
    def test_proportion_invalid_year(self,mock_datasource):
        """Test invalid year input"""
        mock_datasource_inst = mock_datasource.return_value
        mock_datasource_inst.get_usage_percentage.return_value = None
        with self.assertRaises(IndexError):
            usage_proportion("Argentina", "3023")

    def test_proportion_no_year(self):
        """Test missing year input"""
        sys.argv = ["command_line.py", "-usageproportion", "Argentina"]
        printed_out = self._run_and_return_output()
        self.assertEqual(
            printed_out,
            print_help_statement().strip(),
        )


if __name__ == "__main__":
    main()
