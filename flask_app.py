"""
Flask application for global water usage analysis.
"""

from flask import Flask, Blueprint
from ProductionCode.use_time_compare import water_use_time_compare
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.per_capita import print_per_capita_water_use

app = Flask(__name__)
api = Blueprint('api', __name__)

@app.route('/')
def home():
    """
    Returns instructions with available API endpoints
    """
    welcome_message = """Welcome to the Global Water Usage Analysis API!

    Use the following routes:

        1. Water Usage Over Time
        Format: /api/water_use/country/year_1/year_2/
        Description: Compare water usage between two years
        Example: /api/water_use/USA/2018/2020/

        2. Usage Proportion by Sector
        Format: /api/usage_proportion/country/year/
        Description: Water usage breakdown (Agricultural, Industrial, Household)
        Example: /api/usage_proportion/Argentina/2023/

        3. Per Capita Water Usage
        Format: /api/per_capita/country/year/
        Description: Average water usage per capita (liters per day)
        Example: /api/per_capita/Argentina/2023/

        Notes:
        • Available years: 2000-2024 (depends on data availability)
        • Country names support aliases (USA, US, UK, etc.)
        • Country names are case-insensitive
        """
    return f'<pre>{welcome_message}</pre>'

@api.route('/water_use/<country>/<year1>/<year2>/')
def water_use_route(country, year1, year2):
    """
    Returns water usage comparison between two years for a given country.
    """
    try:
        result = water_use_time_compare(country, year1, year2)
        return result
    except (ValueError, KeyError) as e:
        return f"Error: {str(e)}"


@api.route('/usage_proportion/<country>/<year>/')
def usage_proportion_route(country, year):
    """
    Returns water usage proportion by sector for a given country and year.
    """
    try:
        result = usage_proportion(country, year)
        return result
    except (ValueError, KeyError) as e:
        return f"Error: {str(e)}"

@api.route('/per_capita/<country>/<year>/')
def per_capita_route(country, year):
    """
    Returns per capita water usage for a given country and year.
    """
    try:
        value = print_per_capita_water_use(country, year)
        return value
    except (ValueError, KeyError) as e:
        return f"Error: {str(e)}"

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with helpful information.
    """
    text = str(e)+"""error: 404 - Page Not Found

    The page you're looking for doesn't exist. Please check the URL and try again.

    - /api/water_use/country/year_1/year_2/
    - /api/usage_proportion/country/year/
    - /api/per_capita/country/year/

    Visit the homepage (/) for detailed instructions and examples.
    """
    return f'<pre>{text}</pre>'

def main():
    """Main function to run the Flask app."""
    app.register_blueprint(api, url_prefix='/api')
    app.run(port=5107)

if __name__ == '__main__':
    main()
