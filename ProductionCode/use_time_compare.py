"""
Functions for the temporal comparison of water usage data
"""

from ProductionCode.database import DB, filter_tags_database
from ProductionCode.utils import alias

def water_use_time_compare(country: str, year1: int, year2: int) -> str:
    """
    Compares the water use of a country between 2 years
    
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @return : Formatted string comparing water use between the two years
    """
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
    out = water_use_time_compare_format(country, year1, year2, water_use_y1, water_use_y2)
    return out

def water_use_time_compare_print(out):
    """Prints the water use time compare
    @param out: The output string from water_use_time_compare
    """
    print(out)


def water_use_time_compare_format(country, year1, year2, wu1, wu2):
    """
    @param country: The country to compare water use for
    @param year1: The first year to compare
    @param year2: The second year to compare
    @param wu1: Water use in year1
    @param wu2: Water use in year2
    @return: Formatted string comparing water use between the two years
    """
    out = "Water usage in " + country
    out += "\n" + str(year1) + ": " + wu1 + "x10^9 cubic meters/year"
    out += "\n" + str(year2) + ": " + wu2 + "x10^9 cubic meters/year"
    out += "\n" + "Difference:"
    out += "\n" + str(int(wu2) - int(wu1)) + "x10^9 cubic meters/year"
    return out
