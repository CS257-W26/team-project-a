"""
Functions for the per capita analysis of water usage data
"""

from ProductionCode.database import DataSource
from ProductionCode.utils import alias


def get_per_capita_water_use(country: str, year: str) -> float:
    """Returns per capita water use (liters per day) for a given country and year.
    
    @param country: The country to get per capita water use for
    @param year: The year to get per capita water use for
    @return: Per capita water use in liters per day"""
    if not str(year).isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    filtered_data = DataSource().get_per_capita(country,year)
    if filtered_data:
        return float(round(filtered_data, 2))
    raise IndexError(
        "Country or year not found. Please pick another country or pick years from 2000-2024."
    )
