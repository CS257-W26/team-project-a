"""
Functions for the use-type proportions analysis of water usage data
"""

from ProductionCode.database import DB, filter_tags_database, DataSource
from ProductionCode.utils import alias

def validate_year(year: str) -> None:
    """
    Validate year input.
    """
    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

def fetch_usage_row(country: str, year: str) -> list:
    """
    Fetch a single usage row for the given country and year.

    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The row of data for the specified country and year
    """
    filtered_data = filter_tags_database(DB.CLEANED_GWC, [str(country), str(year)])
    if len(filtered_data) == 0:
        raise ValueError(
            "Country or year not found. Pick another country or pick years from 2000-2024."
        )
    return filtered_data[0]

def select_usage_percentage(row: list, usagetype: str) -> float:
    """
    Select a usage percentage from a row by type.

    @param row: The row of data to select from
    @param usagetype: The type of usage to get percentage for
    @return: The percentage of water usage for the given usage type
    """
    if usagetype == "Agricultural":
        return float(row[4])
    if usagetype == "Industrial":
        return float(row[5])
    if usagetype == "Household":
        return float(row[6])
    raise ValueError(
        "Usage type not found. Use 'Agricultural', 'Industrial', or 'Household'."
    )

def usage_proportion(country, year):
    """
    Determines water usage proportions by sector for a given country and year.

    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @return: The water usage proportions for the given country and year
    """

    """
    agc_percent = get_usage_percentage(country, year, "Agricultural")
    ind_percent = get_usage_percentage(country, year, "Industrial")
    hsh_percent = get_usage_percentage(country, year, "Household")
    """
    agc_percent = DataSource.run_string_psql("SELECT agr_total FROM GLOBALDATA_S WHERE yr = " + year + " AND country = ’"+country+"’;")
    ind_percent = DataSource.run_string_psql("SELECT ind_total FROM GLOBALDATA_S WHERE yr = " + year + " AND country = ’"+country+"’;")
    hsh_percent = DataSource.run_string_psql("SELECT hou_total FROM GLOBALDATA_S WHERE yr = " + year + " AND country = ’"+country+"’;")

    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(agc_percent, 2)) + "%\n" + \
            "Industrial:" + str(round(ind_percent, 2)) + "%\n" + \
                "Household:" + str(round(hsh_percent, 2)) + "%\n")


def get_usage_percentage(country: str, year: str, usagetype) -> float:
    """
    Gets the percentage of water usage for a given usage type in a specified country and year.
    
    @param country: The country to get usage proportions for
    @param year: The year to get usage proportions for
    @param usagetype: The type of usage to get percentage for
    @return: The percentage of water usage for the given usage type 
    in the specified country and year
    """

    validate_year(year)
    country = alias(country)
    row = fetch_usage_row(country, year)
    return select_usage_percentage(row, usagetype)
