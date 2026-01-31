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
