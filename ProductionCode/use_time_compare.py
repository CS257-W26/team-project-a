"""
Functions for the temporal comparison of water usage data
"""

from ProductionCode.database import DataSource
from ProductionCode.utils import alias

def validate_years(year1: int, year2: int) -> None:
    """
    Validate years are within range.
    @param year1: The first year
    @param year2: The second year
    """
    if not 2000 <= int(year1) <= 2024 or not 2000 <= int(year2) <= 2024:
        raise ValueError("Years must be between 2000 and 2024.")
def get_water_use(country: str, year: int) -> float:
    """
    Fetch water use for a country and year from the cleaned dataset.
    @param country: The country to get water use for
    @param year: The year to get water use for
    @return: Water use in billion cubic meters/year"""
    return DataSource().get_total_resources(country,year)

def water_use_time_compare(country: str, year1: int, year2: int) -> str:
    """
    Compares the water use of a country between 2 years
    
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @return : Array of values for the resulting data.
    [0: country, 1: year1, 2: year2, 3: WU1, 4: WU2]
    """
    validate_years(year1, year2)
    country = alias(country)
    water_use_y1 = get_water_use(country, year1).total_resources
    water_use_y2 = get_water_use(country, year2).total_resources
    return [country,str(year1),str(year2),str(water_use_y1),str(water_use_y2)]

def print_water_use_time_compare(arr: []):
    """Prints the water use time compare
    @param out: The output string from water_use_time_compare
    """
    print(format_water_use_time_compare(arr))


def format_water_use_time_compare(arr: []):
    """
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @param wu1: Water use in year1
    @param wu2: Water use in year2
    @return: Formatted string comparing water use between the two years
    """
    country = arr[0]
    year1 = int(arr[1])
    year2 = int(arr[2])
    wu1 = int(arr[3])
    wu2 = int(arr[4])
    out = "Water usage in " + country
    out += "\n" + str(year1) + ": " + str(round(wu1, 2)) + " billion cubic meters/year"
    out += "\n" + str(year2) + ": " + str(round(wu2, 2)) + " billion cubic meters/year"
    out += "\n" + "Difference:"
    out += "\n" + str(round(wu2 - wu1, 2)) + " billion cubic meters/year"
    return out
