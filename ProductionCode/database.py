"""
Database operations for water usage data.
Handles CSV file management and data filtering.
"""

import records
import ProductionCode.psql_config as config
class DataSource:
    '''Main datsource class, connecting to databse & running/printing the example'''
    def __init__(self):
        '''Constructor that initiates connection to database'''
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5432/{config.DATABASE}"
        self.db = records.Database(connect)

    def run_string_psql(self, str_command):
        '''
        Takes in self and a string equating to a psql command
        (for example "SELECT * FROM AQTE;")
        Prints the result of that command being run
        '''
        result = self.db.query(str_command)
        if len(result.all()) > 0:
            return result[0]
        raise IndexError

    def run_string_psql_multiple(self, str_command):
        '''
        Takes in self and a string equating to a psql command
        (for example "SELECT * FROM AQTE;")
        Prints the result of that command being run
        '''
        result = self.db.query(str_command)
        return result

    def get_per_capita(self,country: str, year: int):
        '''
        Takes a country and year and returns it's per capita water use.
        (eg: get_per_capita("USA",2001))
        '''
        return self.run_string_psql\
        ("SELECT per_capita FROM GLOBALDATA_S WHERE country = '"+country+"' AND yr = "+str(year)\
            +";").per_capita

    def get_usage_percentage(self,country: str,year:int,mode:int):
        '''
        Takes a country, year, and mode and returns that industries
        percentage use.
        (eg: get_usage_percentage("USA",2001,1))
        0 = agricultural
        1 = industrial
        2 = household/domestic
        '''
        if mode == 0:
            return self.run_string_psql("SELECT agr_total FROM GLOBALDATA_S WHERE\
                yr = " + str(year) + " AND country = '"+country+"';").agr_total
        if mode == 1:
            return self.run_string_psql("SELECT ind_total FROM GLOBALDATA_S WHERE\
                yr = " + str(year) + " AND country = '"+country+"';").ind_total
        if mode == 2:
            return self.run_string_psql("SELECT hou_total FROM GLOBALDATA_S WHERE\
                yr = " + str(year) + " AND country = '"+country+"';").hou_total
        raise ValueError()

    def get_total_resources(self,country: str,year:int):
        '''
        Takes a country and year and returns it's total exploitable water
        resoruces.
        (eg: get_total_resources("USA",2001))
        '''
        return self.run_string_psql("SELECT total_resources FROM AQTE WHERE country = '"+\
        country+"' AND yr = "+str(year)+";")

    def get_countries(self, dataset1:str):
        '''
        Returns a list of all the countries in the database.
        '''
        result = self.run_string_psql_multiple("SELECT DISTINCT country FROM "+dataset1+";")
        return [row.country for row in result]