# Title
Global Water Sources v Spending

# Sustainable Development Goal(s)
Responsible consumption & production
Clean water & sanitation

# Features
* Ability to compare how a country obrains its water resources v. how they spend those resources (interactable visual graph)
* Interactable Global Map w/ data
* Small dictionary (not the coding kind, the kind where you ask about the meanings of terms)

## Feature 1: Identify proportonality of country's water usage

* Person responsible: Lloyd
* User story: I input Canada to see what percentage of it's water is going to Agricultutal usage, Industrial usage and Household usage and find that the cooresponding percentages for the most recent year are 57%, 26.7%, 26.4%
* Acceptance Criteria: User can input "country_usage_breakdown canada" and it responds with the dates (accurate for the current year) of "Agricultral: 57%, Industrial: 26.7%, Household: 26.4%

## Feature 2: Country per capita water usage

* Person responsible: Paul
* User story: As someone intersted in Japan's water usage, I want to compare Japan's average water use per capita in 2018, so that I can learn how much water an average person uses.
* Acceptance Criteria: 
    - User can input "python3 command_line.py Japan perCapita 2018". 
    - If the year or country is not available, give an error message saying pick another country or pick years from 2000-2024.
    - The numbers pulled from dataset will corresspond to the user's input and be displayed. 
    - Output: Japan's Water Usage per Capita: 290.58 Liters per day

## Feature 3: Water usage over time
* Person responsible: Jay
* User story: I want to find out how the water usage in the US has changed over the last 3 years. I can give a country and 2 years to the CLI and it will return how water usage has changed.
* Acceptance Criteria: User can input "python3 command_line.py US 2022 2025" and will recive the values of water usage for those two years, as well as how they've changed.

# Datasets Metadata
* Name: FAO AQUASTAT Dissemination System
    - URL: https://data.apps.fao.org/aquastat/?lang=en
    - Downloaded: 01/12/26
    - Authorship: Food and Agriculture Organization
    - Terms and Conditions: https://www.fao.org/contact-us/terms/en

* Name: Global Water Consumption Dataset (2000-2024) 🌍💧
    - URL: https://www.kaggle.com/datasets/atharvasoundankar/global-water-consumption-dataset-2000-2024
    - Downloaded:  01/12/26
    - Authorship: Atharva Soundankar
    - Terms and Conditions: CC0:Public Domain

# Mock up
Sketches have been included.

# Data story
Hi! Lloyd typing! 
Originally Jay wanted to do something involving water waste due to cooling. When me and Paul met, we were talking about this water thing and began to do research. This research eventually led me to realize that the word "withdrawl" was being used in a confusing way, both as "where water is being taken from" and "where water is being used". Thus came the idea to start comparing those two datapoints. 

The first dataset was found mostly by me attempting to track down "breakdowns of what kinds of water sources people get water from" and this was not only essentially the only global data on the subject but also incredibly verbose about practically everything you could want to know on the subject. The second was found significantly earlier in the search but it covers data in more general terms than the first (the over-complexity of the first is arguably it's biggest flaw and we are not even using the whole thing.)