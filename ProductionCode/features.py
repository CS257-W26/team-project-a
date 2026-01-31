"""
Feature analysis functions for water usage data.
"""

from ProductionCode.database import DB, filter_tags_database, filter_by_tags, open_database
from ProductionCode.utils import alias

def water_use_time_compare(country: str, year1: int, year2: int):
    """Compares the water use of a country between 2 years"""
    country = alias(country)

    time1 = filter_tags_database(
        DB.AQS_WR,
        [
            str(country),
            str(year1),
            "Exploitable water resources and dam capacity",
            "Total exploitable water resources"
        ],
    )
    time2 = filter_tags_database(
        DB.AQS_WR,
        [
            str(country),
            str(year2),
            "Exploitable water resources and dam capacity",
            "Total exploitable water resources"
        ],
    )

    if len(time1) == 0 or len(time2) == 0:
        print("One of these years is not present in the database!")
        raise KeyError
    time1 = time1[0]
    time2 = time2[0]

    water_use_y1 = time1[6].strip()
    water_use_y2 = time2[6].strip()
    water_use_time_compare_print(country,year1,year2,water_use_y1,water_use_y2)

def water_use_time_compare_print(country,year1,year2,wu1,wu2):
    """Prints the water use time compare"""
    print("Water usage in " + country, "\n")
    print(str(year1) + ": " + wu1 + "x10^9 cubic meters/year")
    print(str(year2) + ": " + wu2 + "x10^9 cubic meters/year")
    print("Difference:")
    print(str(int(wu2) - int(wu1)) + "x10^9 cubic meters/year")

def usage_proportion(country, year):
    """Returns the proportial usage of Agricultural, \
    Industrial and Household water usage in terms of percentage"""

    agc_percent = get_usage_percentage(country, year, "Agricultural")
    ind_percent = get_usage_percentage(country, year, "Industrial")
    hsh_percent = get_usage_percentage(country, year, "Household")

    return("Water usage in " + str(country) + " in " + str(year) + "\n" + \
           "Agricultural:" + str(round(agc_percent, 2)) + "%\n" + \
            "Industrial:" + str(round(ind_percent, 2)) + "%\n" + \
                "Household:" + str(round(hsh_percent, 2)) + "%\n")

def get_per_capita_water_use(country: str, year: str) -> float:
    """Returns per capita water use (liters per day) for a given country and year,\
    Raises ValueError if country/year not found or year out of range"""
    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = open_database(DB.CLEANED_GWC)

    tags = [country, year]
    
    filtered_data = filter_by_tags(data, tags)
    if len(filtered_data) > 0:
        return float(filtered_data[0][3])
    raise ValueError(
        "Country or year not found. Pick another country or pick years from 2000-2024."
    )

def get_usage_percentage(country: str, year: str, usagetype) -> float:
    """Returns percentage for usage for a given country and year.\
    Raises ValueError if country/year not found or year out of range"""

    if not year.isdigit() or not 2000 <= int(year) <= 2024:
        raise ValueError("Year must be between 2000 and 2024.")

    country = alias(country)
    data = open_database(DB.CLEANED_GWC)

    # Skip header row
    for row in data[1:]:
        if row[0] == country and row[1] == year:  # match country and year
            if usagetype == "Agricultural":
                return float(row[4])
            if usagetype == "Industrial":
                return float(row[5])
            if usagetype == "Household":
                return float(row[6])

    raise ValueError(
        "Country, year or usage type not found. "
        "Pick another country or pick years from 2000-2024 and make sure you are inputting \
        'Agriculture', 'Industrial' or 'Household'."
    )
