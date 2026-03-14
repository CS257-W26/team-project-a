"""
Functions for the use-type proportions analysis of water usage data
"""

from ProductionCode.database import DataSource
from ProductionCode.utils import alias

def get_countries():
    """
    Fetches the list of countries from the cleaned dataset.
    @return: List of country names
    """
    return DataSource().get_countries("GLOBALDATA_S")

def get_usage_proportion(country: str, year: int) -> str:
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
    return{
        "Agricultural": round(agricultural_percent, 2),
        "Industrial": round(industrial_percent, 2),
        "Household": round(household_percent, 2)
    }


def usage_proportion(country, year):
    """
    Determines water usage proportions by sector for a given country and year.

    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The water usage proportions for the given country and year
    """
    usage_data = get_usage_proportion(country, year)
    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(usage_data["Agricultural"], 2)) + "%\n" + \
            "Industrial:" + str(round(usage_data["Industrial"], 2)) + "%\n" + \
                "Household:" + str(round(usage_data["Household"], 2)) + "%\n")
