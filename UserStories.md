1.
* User story: As a person intrested in Canada's usage of water for different reasons 2023, I can look up Canada's water usage proportions and find the percentages for industrial, agricultural, and household.
* Acceptance Criteria (CLI): User can input "python3 command_line.py -usageproportion Canada 2023" and it responds with the percentages for Agricultural, Industrial, and Household usage. (Agricultural:50.0%, Industrial:23.55%, Household:26.95%)
* Acceptance Criteria (Web/API): User can access "/api/usage_proportion/Canada/2023/" and it returns the same result.

2.
* User story: As a person who wants to understand how much water the average person in Japan uses per year, I can search for Japan's per-capita water use in 2018 to find out how much the average person uses.
* Acceptance Criteria (CLI):
    - User can input "python3 command_line.py -percapita Japan 2018".
    - If the year or country is not available, the system displays an error message.
    - Output: "Japan's Water Usage per Capita: 290.58 Liters per day"
* Acceptance Criteria (Web/API): User can access "/api/per_capita/Japan/2018/" and it returns the same result.

3.
* User story: As a person who wants to figure out if America has increased it's water use from 2018-2020, I can search America, as well as two dates, to find out how much the water usage has changed.
* Acceptance Criteria (CLI): User can input "python3 command_line.py -usageovertime US 2018 2020" and it returns the values for 2018 and 2020 plus the difference. (2018: 1829.0 billion cubic meters/year, 2020: 1829.0 billion cubic meters/year, 0.0 billion cubic meters/year difference)
* Acceptance Criteria (Web/API): User can access "/api/water_use/US/2018/2020/" and it returns the same resut.