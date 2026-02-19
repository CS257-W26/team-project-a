"""
Functions for the use-type proportions analysis of water usage data
"""

from ProductionCode.database import DataSource
from ProductionCode.utils import alias

def validate_year(year: str) -> None:
    """
    Validate year input.
    """
    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

def usage_proportion(country, year):
    """
    Determines water usage proportions by sector for a given country and year.

    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The water usage proportions for the given country and year
    """
    source = DataSource()
    country = alias(country)
    agc_percent = source.select_usage_percentage(country,year,0)
    ind_percent = source.select_usage_percentage(country,year,1)
    hsh_percent = source.select_usage_percentage(country,year,2)
    print(agc_percent)
    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(agc_percent, 2)) + "%\n" + \
            "Industrial:" + str(round(ind_percent, 2)) + "%\n" + \
                "Household:" + str(round(hsh_percent, 2)) + "%\n")
