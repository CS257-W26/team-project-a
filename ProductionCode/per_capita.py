"""
Functions for the per capita analysis of water usage data
"""

from ProductionCode.database import DB, filter_tags_database
from ProductionCode.utils import alias


def get_per_capita_water_use(country: str, year: str) -> float:
    """Returns per capita water use (liters per day) for a given country and year.
    
    @param country: The country to get per capita water use for
    @param year: The year to get per capita water use for
    @return: Per capita water use in liters per day"""
    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    filtered_data = filter_tags_database(DB.CLEANED_GWC, [country, year])
    if len(filtered_data) > 0:
        return float(filtered_data[0][3])
    raise ValueError(
        "Country or year not found. Pick another country or pick years from 2000-2024."
    )

def print_per_capita_water_use(country: str, year: str):
    """
    Prints per capita water use for a given country and year
    @param country: The country to get per capita water use for
    @param year: The year to get per capita water use for
    @return: Formatted string of per capita water use
    """
    value = get_per_capita_water_use(country, year)
    return(
        f"{alias(country)}'s Water Usage per Capita: {round(value, 2)} Liters per day"
    )
