"""
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
"""

import sys
from ProductionCode.per_capita import get_per_capita_water_use
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.use_time_compare import water_use_time_compare, print_water_use_time_compare

from ProductionCode.utils import print_help_statement, check_arg_count


def main():
    """Main func"""
    if len(sys.argv) <= 1:
        print_help_statement()
        return
    mode = sys.argv[1].lower()
    if mode == "-usageovertime":
        if not check_arg_count(len(sys.argv), 5):
            return
        out = water_use_time_compare(sys.argv[2], sys.argv[3], sys.argv[4])
        print_water_use_time_compare(out)
    elif mode == "-percapita":
        if not check_arg_count(len(sys.argv), 4):
            return
        try:
            value = get_per_capita_water_use(sys.argv[2], sys.argv[3])
            print(f"{value} Liters per day")
            return
        except ValueError as e:
            print(e)
    elif mode == "-usageproportion":
        if not check_arg_count(len(sys.argv), 4):
            return
        try:
            print(usage_proportion(sys.argv[2], sys.argv[3]))
        except ValueError as e:
            print(e)
    elif mode == "-help":
        print_help_statement()
    else:
        print_help_statement()
    return


if __name__ == "__main__":
    main()
