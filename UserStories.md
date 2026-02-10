1.
* User story: Given the user wants to see what percentage of Canada's water is going to Agricultural usage, Industrial usage, and Household usage in 2023, the system returns the three percentages.
* Acceptance Criteria (CLI): User can input "python3 command_line.py -usageproportion Canada 2023" and it responds with the percentages for Agricultural, Industrial, and Household usage.
* Acceptance Criteria (Web/API): User can access "/api/usage_proportion/Canada/2023/" and it returns the same result.

2.
* User story: Given the user wants to know the average water usage per capita for Japan in 2018, the output value is 290.58 liters per day.
* Acceptance Criteria (CLI):
    - User can input "python3 command_line.py -percapita Japan 2018".
    - If the year or country is not available, the system displays an error message.
    - Output: "Japan's Water Usage per Capita: 290.58 Liters per day"
* Acceptance Criteria (Web/API): User can access "/api/per_capita/Japan/2018/" and it returns the same result.

3.
* User story: Given the user wants to compare water usage in the United States of America between 2018 and 2020, the system returns values for both years and their difference.
* Acceptance Criteria (CLI): User can input "python3 command_line.py -usageovertime US 2018 2020" and it returns the values for 2018 and 2020 plus the difference.
* Acceptance Criteria (Web/API): User can access "/api/water_use/US/2018/2020/" and it returns the same resut.