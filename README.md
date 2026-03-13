[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/w6LgLvZq)
# CS257-TeamTemplate
Template for long-term team projects for CS257 Software Design

## Features

### Feature 1: Identify Proportionality of Country's Water Usage
This feature allows users to see the breakdown of a country's water usage by sector (Agricultural, Industrial, and Household) for an inputted year.

**Command:** `python3 command_line.py -usageProportion --country --year`  
**Example:** `python3 command_line.py -usageProportion Argentina 2024`  
**Output:** Water usage in Argentina in 2024 Agricultural:51.2% Industrial:34.14% Household:23.52%

Alternatively, one can use Flask. By running the Flask program and updating the url one can obtain the same result
**URL Addition:** `/usage_proportion/<country>/<year>`
**Example:** `/usage_proportion/Argentina/2024`
**Output:** Water usage in Argentina in 2024 Agricultural:51.2% Industrial:34.14% Household:23.52%

### Feature 2: Country Per Capita Water Usage
This feature provides the average water usage per capita for a specified country and year.

**Command:** `python3 command_line.py -perCapita --country --year`  
**Example:** `python3 command_line.py -perCapita Japan 2018`  
**Output:** Japan's Water Usage per Capita: 290.58 Liters per day

If the year or country is not available, an error message will suggest selecting another country or years from 2000-2024.

Alternatively, one can use Flask. By running the Flask program and updating the url one can obtain the same result
**URL Addition:** `/per_capita/<country>/<year>`
**Example:** `/per_capita/Japan/2018`
**Output:** Japan's Water Usage per Capita: 290.58 Liters per day

### Feature 3: Water Usage Over Time
This feature compares a country's water usage between two specified years, showing the values for each year and the change over time.

**Command:** `python3 command_line.py -usageovertime --country --year1 --year2`  
**Example:** `python3 command_line.py -usageovertime US 2003 2004`  
**Output:** Water usage in United States of America 2003: 25 billion m^3/year 2004: 26 billion m^3/year Difference: 1 billion m^3/year

Alternatively, one can use Flask. By running the Flask program and updating the url one can obtain the same result
**URL Addition:** `/water_use/<country>/<year1>/<year2>`
**Example:** `/water_use/US/2003/2004`
**Output:** Water usage in United States of America 2003: 25 billion m^3/year 2004: 26 billion m^3/year Difference: 1 billion m^3/year


## How to Use the Commands
Type in `python3 command_line.py` followed by the appropriate arguments for the feature you want to use, separated by spaces.  
For example: `python3 command_line.py -perCapita Brazil 2020`

## Dependancies
* csv - Used to read in the CSV database files
* sys - Used to interact with argv and read/write to arguments for testing and CLI purposes. 
* enum - Used to simplify choosing database files
- Testing -
* unittest - Standard python test framework
* StringIO - Used to read stdout for testing

## Website Organization/Design
The website has a very clear design which enables easy reading for someone who's quickly looking at the website
* Title of site in the top left in the header. Header is distinct, words are clickable (change shades when hovered, in a conventional location)
* Header also contains links to the home page (Water Usage Search), compare page and about. (Headers consistent throughout pages)
* Specific pages have a large well-defined form in the middle (promotes Scanning)
* Buttons on the form and ability to search are clearly clickable, buttons are well defined. (promotes Scanning)
* Due to how few things there are on the website, it's hard to miss what is being shown. Simplistic & polished. (this promotes Satisficing/Muddling Through)


# Reworks
- J: Reworked the method for obtaining use time compare

## TD5 Improvements
# Option A: Code Design Improvements
* Implementation of a DataSource Singleton
    - What was the issue?
        Before implementing the singleton pattern, each call to DataSource() could create a new database connection. Since the project calls DataSource() from multiple locations, this led to unnecessary connection creation and made shared access to the database harder to manage and reason about.
    - What were the specific files/lines that were changed?
        The singleton implementation was added to the DataSource class in ProductionCode/database.py, specifically around lines 17–22, where the __new__ method and class-level instance variable were introduced.
    - How did the change happen?
        The DataSource class now maintains a class-level instance variable and overrides the __new__ method to ensure that only one instance of the class can be created. The first time DataSource() is called, the object is created and the database connection is initialized in __init__. Any new calls return the same existing instance instead of creating a new one. This centralizes database access and prevents repeatedly creating new database objects.

# Option B: Front End Design Improvements
* Drop-down order and ease of use
    - What was the issue?
        Drop down menus for lists of countries (both on the main page and the compare page) were not listed in alphabetical order. There were also many combinations of countries (Subsaharan Africa, Oceania minus Australia, Impoverished Island Nations, etc.) in the Compare stats' list that made an already excessive list more bloated. Both dropdowns were hard to navigate, especially in the context of people using the website in user testing.
    - What were the specific files/lines that were changed? How were they changed?
        For the first issue, line 94 of database.py in ProductionCode was changed to include "ORDER BY country ASC". For the removal of the countries, this actually was done outside of the code and was done manually in the csv itself. This was something that was smoother to do by hand than through SQL.
* Improvements in satisficing
    - What was the issue?
    - What were the specific files/lines that were changed?
    - How did the change happen?