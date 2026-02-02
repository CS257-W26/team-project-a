"""
Functions for the use-type proportions analysis of water usage data
"""

from ProductionCode.database import DB, filter_tags_database
from ProductionCode.utils import alias

def usage_proportion(country, year):
    """
    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The water usage proportions for the given country and year
    """

    agc_percent = get_usage_percentage(country, year, "Agricultural")
    ind_percent = get_usage_percentage(country, year, "Industrial")
    hsh_percent = get_usage_percentage(country, year, "Household")

    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(agc_percent, 2)) + "%\n" + \
            "Industrial:" + str(round(ind_percent, 2)) + "%\n" + \
                "Household:" + str(round(hsh_percent, 2)) + "%\n")

def get_usage_percentage(country: str, year: str, usagetype) -> float:
    """
    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @param usagetype: The type of usage to get percentage for
    @return: The percentage of water usage for the given usage type 
    in the specified country and year
    """

    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)

    filtered_data = filter_tags_database(
        DB.CLEANED_GWC,
        [
            str(country),
            str(year)
        ],
    )
    if len(filtered_data) > 0:
        if usagetype == "Agricultural":
            return float(filtered_data[0][4])
        if usagetype == "Industrial":
            return float(filtered_data[0][5])
        if usagetype == "Household":
            return float(filtered_data[0][6])
    raise ValueError(
        "Country, year or usage type not found. "
        "Pick another country or pick years from 2000-2024 and make sure you are inputting \
        'Agriculture', 'Industrial' or 'Household'."
    )
