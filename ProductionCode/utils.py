"""
Utility functions for string formatting and aliases.
"""

def alias(var: str) -> str:
    """Used to make it so that country names don't have to be input perfectly.
    
    @param var: The country name input by the user
    @return: The standardized country name
    """
    match var.lower():
        case "usa" | "us" | "united states" | "united states of america" | "america":
            return "United States of America"
        case "uk" | "UK" | "united kingdom":
            return "United Kingdom"
        case _:
            return var


def check_arg_count(actual_count: int, expected_count: int) -> bool:
    """
    Check if the number of arguments matches the expected count.

    @param actual_count: Number of arguments passed in
    @param expected_count: Number of arguments expected
    @return: True if counts match, False otherwise
    """
    if actual_count != expected_count:
        print_help_statement()
        return False
    return True

def print_help_statement():
    """Returns help information for the command line interface"""
    help_text = """COMMANDS:
    -usageproportion <country> <year>
        Shows water usage breakdown by sector (Agricultural, Industrial, Household)
        Example: python3 command_line.py -usageproportion Argentina 2024

    -percapita <country> <year>
        Shows average water usage per capita (liters per day)
        Example: python3 command_line.py -percapita Japan 2018

    -usageovertime <country> <year1> <year2>
        Compares water usage between two years
        Example: python3 command_line.py -usageovertime US 2003 2004

    NOTES:
    • Available years: 2000-2024
    • Country names support aliases (USA, UK, etc.)"""
    print(help_text)
    return help_text