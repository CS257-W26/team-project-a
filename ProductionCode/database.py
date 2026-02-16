"""
Database operations for water usage data.
Handles CSV file management and data filtering.
"""

import csv
from enum import Enum
import ProductionCode.psql_config as config
import records

class DataSource:
    '''Main datsource class, connecting to databse & running/printing the example'''
    def __init__(self):
        '''Constructor that initiates connection to database'''
        connect = f"postgresql://{config.USER}:{config.PASSWORD}@localhost:5111/{config.DATABASE}"
        self.db = records.Database(connect)

    def run_string_psql(self, str_command):
        '''
        Takes in self and a string equating to a psql command
        (for example "SELECT * FROM AQTE;")
        Prints the result of that command being run
        '''
        result = self.db.query(str_command)
        return(result[0])

    def run_string_psql_multiple(self, str_command):
        '''
        Takes in self and a string equating to a psql command
        (for example "SELECT * FROM AQTE;")
        Prints the result of that command being run
        '''
        result = self.db.query(str_command)
        return(result)
        

class DB(Enum):
    """Enum for databases"""

    AQS_DS3 = "Data/AQUASTAT Dissemination System (3).csv"
    AQS_DS6 = "Data/AQUASTAT Dissemination System (6).csv"
    AQS_WR = "Data/AQUASTAT-Water Resources.csv"
    AQS_WU = "Data/AQUASTAT-Water Use.csv"
    CLEANED_GWC = "Data/cleaned_global_water_consumption 2.csv"
    DATABASES = [AQS_DS3,AQS_DS6,AQS_WR,AQS_WU,CLEANED_GWC]

def id_to_db(iden:int) -> DB:
    """Maps integer IDs to enum values."""
    if iden == 0:
        return DB.AQS_DS3
    if iden == 1:
        return DB.AQS_DS6
    if iden == 2:
        return DB.AQS_WR
    if iden == 3:
        return DB.AQS_WU
    if iden == 4:
        return DB.CLEANED_GWC

    raise IndexError


def open_database(database: DB):
    """
    Returns an array for the spesificed database. EG: open_database(DB.AQS_DS3)
    
    @param database: The database to open
    @return: List of the database contents
    """
    if database not in list(DB):
        raise KeyError
    arr = []
    with open(database.value, newline="",encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in reader:
            arr.append(row)
        return arr

def filter_by_tags(db: [], tags: []):
    """Finds all instances in a DB with certain string args
    
    @param db: The database to filter
    @param tags: The tags to filter by
    @return: List of rows matching the tags
    """
    arr = []
    for row in db:
        matches = True
        for tag in tags:
            if tag not in row:
                matches = False
                break
        if matches:
            arr.append(row)

    return arr

def filter_tags_database(database: DB, tags: []):
    """
    Takes a database (enum) and an array of string tags. Returns all matches from\
    the spesified DB. EG: filter_by_tagsDB(DB.CLEANED_GWC,['USA','2001'])
    
    @param database: The database to filter
    @param tags: The tags to filter by
    @return: List of rows matching the tags"""
    arr = open_database(database)
    return filter_by_tags(arr, tags)
