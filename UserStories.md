1.
* User story: I input Canada to see what percentage of it's water is going to Agricultutal usage, Industrial usage and Household usage and find that the cooresponding percentages for the most recent year are 57%, 26.7%, 26.4%
* Acceptance Criteria: User can input "country_usage_breakdown canada" and it responds with the dates (accurate for the current year) of "Agricultral: 57%, Industrial: 26.7%, Household: 26.4%

2.
* User story: As someone intersted in Japan's water usage, I want to compare Japan's average water use per capita in 2018, so that I can learn how much water an average person uses.
* Acceptance Criteria: 
    - User can input "python3 command_line.py Japan perCapita 2018". 
    - If the year or country is not available, give an error message saying pick another country or pick years from 2000-2024.
    - The numbers pulled from dataset will corresspond to the user's input and be displayed. 
    - Output: Japan's Water Usage per Capita: 290.58 Liters per day

3.
* User story: I want to find out how the water usage in the US has changed over the last 3 years. I can give a country and 2 years to the CLI and it will return how water usage has changed.
* Acceptance Criteria: User can input "python3 command_line.py US 2022 2025" and will recive the values of water usage for those two years, as well as how they've changed.