"""
Functions for the use-type proportions analysis of water usage data
"""

from ProductionCode.database import DataSource
from ProductionCode.utils import alias

def usage_proportion(country, year):
    """
    Determines water usage proportions by sector for a given country and year.

    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The water usage proportions for the given country and year
    """
    source = DataSource()
    country = alias(country)
    agricultural_percent = source.get_usage_percentage(country,year,0)
    industrial_percent = source.get_usage_percentage(country,year,1)
    household_percent = source.get_usage_percentage(country,year,2)
    if not agricultural_percent or not industrial_percent or not household_percent:
        raise IndexError()
    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(agricultural_percent, 2)) + "%\n" + \
            "Industrial:" + str(round(industrial_percent, 2)) + "%\n" + \
                "Household:" + str(round(household_percent, 2)) + "%\n")
