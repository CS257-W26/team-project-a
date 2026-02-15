from ProductionCode.database import DataSource


def main():
    source = DataSource()
    source.run_string_psql("SELECT * FROM AQTE;")

if __name__ == "__main__":
    main()
