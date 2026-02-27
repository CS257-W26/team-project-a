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
**Output:** Water usage in United States of America 2003: 1829x10^9 cubic meters/year 2004: 1829x10^9 cubic meters/year Difference: 0x10^9 cubic meters/year

Alternatively, one can use Flask. By running the Flask program and updating the url one can obtain the same result
**URL Addition:** `/water_use/<country>/<year1>/<year2>`
**Example:** `/water_use/US/2003/2004`
**Output:** Water usage in United States of America 2003: 1829x10^9 cubic meters/year 2004: 1829x10^9 cubic meters/year Difference: 0x10^9 cubic meters/year


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
