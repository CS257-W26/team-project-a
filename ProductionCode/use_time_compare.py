"""
Functions for the temporal comparison of water usage data
"""

from ProductionCode.database import DB, filter_tags_database, DataSource
from ProductionCode.utils import alias

def validate_years(year1: int, year2: int) -> None:
    """
    Validate years are within range.
    @param year1: The first year
    @param year2: The second year
    """
    if not 2000 <= int(year1) <= 2024 or not 2000 <= int(year2) <= 2024:
        raise ValueError("Years must be between 2000 and 2024.")
def fetch_water_use(country: str, year: int) -> float:
    """
    Fetch water use for a country and year from the cleaned dataset.
    @param country: The country to get water use for
    @param year: The year to get water use for
    @return: Water use in billion cubic meters/year"""
    source = DataSource()
    source.run_string_psql("SELECT total_resources FROM AQTE WHERE country = '"+country+"' AND yr = "+str(year)+";")
    return source.run_string_psql("SELECT total_resources FROM AQTE WHERE country = '"+country+"' AND yr = "+str(year)+";")

def water_use_time_compare(country: str, year1: int, year2: int) -> str:
    """
    Compares the water use of a country between 2 years
    
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @return : Formatted string comparing water use between the two years
    """
    validate_years(year1, year2)
    country = alias(country)
    water_use_y1 = fetch_water_use(country, year1).total_resources
    water_use_y2 = fetch_water_use(country, year2).total_resources
    out = water_use_time_compare_format(country, year1, year2, float(water_use_y1), float(water_use_y2))
    return out

def water_use_time_compare_print(out):
    """Prints the water use time compare
    @param out: The output string from water_use_time_compare
    """
    print(out)


def water_use_time_compare_format(country, year1, year2, wu1, wu2):
    """
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @param wu1: Water use in year1
    @param wu2: Water use in year2
    @return: Formatted string comparing water use between the two years
    """
    out = "Water usage in " + country
    out += "\n" + str(year1) + ": " + str(round(wu1, 2)) + " billion cubic meters/year"
    out += "\n" + str(year2) + ": " + str(round(wu2, 2)) + " billion cubic meters/year"
    out += "\n" + "Difference:"
    out += "\n" + str(round(wu2 - wu1, 2)) + " billion cubic meters/year"
    return out
