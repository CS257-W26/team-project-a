"""
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
"""

import sys
from ProductionCode.database import DB
from ProductionCode.per_capita import get_per_capita_water_use, print_per_capita_water_use
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.use_time_compare import water_use_time_compare, water_use_time_compare_print

from ProductionCode.utils import alias, print_usage_statement


def main():
    """Main func"""
    if len(sys.argv) <= 1:
        print_usage_statement()
        return
    mode = sys.argv[1].lower()
    if mode == "-usageovertime":
        if len(sys.argv) <= 4:
            print("Invalid arguments.")
            return
        out = water_use_time_compare(sys.argv[2], sys.argv[3], sys.argv[4])
        water_use_time_compare_print(out)
    elif mode == "-percapita":
        if len(sys.argv) != 4:
            print_usage_statement()
            return
        try:
            print(print_per_capita_water_use(sys.argv[2], sys.argv[3]))
            return
        except ValueError as e:
            print(e)
    elif mode == "-usageproportion":
        if len(sys.argv) != 4:
            print_usage_statement()
            return
        try:
            print(usage_proportion(sys.argv[2], sys.argv[3]))
        except ValueError as e:
            print(e)
    else:
        print_usage_statement()

    return


if __name__ == "__main__":
    main()
