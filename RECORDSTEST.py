from ProductionCode.database import DataSource
from ProductionCode.use_time_compare import fetch_water_use


def main():
    print(fetch_water_use("Albania",2013))

if __name__ == "__main__":
    main()
