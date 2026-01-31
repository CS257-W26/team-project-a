"""
Utility functions for string formatting and aliases.
"""

def alias(var: str) -> str:
    """Used to make it so that country names don't have to be input perfectly."""
    match var.lower():
        case "usa" | "us" | "united states" | "united states of america" | "america":
            return "United States of America"
        case "uk" | "UK" | "united kingdom":
            return "United Kingdom:"
        case _:
            return var

def print_usage_statement():
    """Prints le usage statement"""
    print("Usage: python3 command_line.py -usageproportion --country --year")
