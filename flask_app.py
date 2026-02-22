"""
Flask application for global water usage analysis.
"""

from flask import Flask, Blueprint
from ProductionCode.use_time_compare import water_use_time_compare
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.per_capita import print_per_capita_water_use
from ProductionCode.database import DataSource

app = Flask(__name__)
api = Blueprint('api', __name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Display homepage with country selection form.

    On GET: renders form with all available countries.
    On POST: renders selected country's water usage data.
    Returns:
        Rendered template with country list and selected data.
    """
    data_source = DataSource()
    names = data_source.get_countries()
    selected_name = ""
    country = None
    error = ""
    year = None

    if request.method == "POST":
        selected_name = request.form.get("country", "")
        if selected_name is None:
            error = "Select a country to view its water usage data."
        else:
            year = request.form.get("year", "")
            
    agc_percent = source.select_usage_percentage(selected_name,year,0)
    ind_percent = source.select_usage_percentage(selected_name,year,1)
    hsh_percent = source.select_usage_percentage(selected_name,year,2)


    return render_template(
        "index.html",
        names=names,
        selected_name=selected_name,
        country_perCapita=get_per_capita_water_use(selected_name, year) if selected_name else None,
        agricultural=agc_percent,
        industrial=ind_percent,
        household=hsh_percent,
        error=error,
        year=year
    )

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
    app.run(port=5100)

if __name__ == '__main__':
    main()
