"""
Flask application for global water usage analysis.
"""

from flask import Flask, Blueprint, request, render_template
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
    names = data_source.get_countries("GLOBALDATA_S")
    selected_name = ""
    error = ""
    year = None
    agricultural_percent = None
    industrial_percent = None
    household_percent = None
    country_per_capita = None

    if request.method == "POST":
        selected_name = request.form.get("country", "")
        year_value = request.form.get("year", "")
        if not selected_name:
            error = "Select a country to view its water usage data."
        elif not year_value:
            error = "Select a year to view its water usage data."
        else:
            try:
                year = int(year_value)
                agricultural_percent = data_source.get_usage_percentage(selected_name, year, 0)
                industrial_percent = data_source.get_usage_percentage(selected_name, year, 1)
                household_percent = data_source.get_usage_percentage(selected_name, year, 2)
                country_per_capita = print_per_capita_water_use(selected_name, year)
            except (ValueError, IndexError):
                error = "Invalid country or year selection."


    return render_template(
        "index.html",
        names=names,
        selected_name=selected_name,
        country_perCapita=country_per_capita,
        agricultural=agricultural_percent,
        industrial=industrial_percent,
        household=household_percent,
        error=error,
        year=year
    )

@app.route('/about')
def about():
    """
    Display the project overview page.
    """
    return render_template("about.html")

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    """
    Display the way of comparing a country over the span of two inputted years.

    On GET: renders form with all available countries.
    On POST: renders selected country/years' water data.
    Returns:
        Rendered template with country list and selected data.
    """
    data_source = DataSource()
    names = data_source.get_countries("AQTE")
    selected_name = ""
    error = ""
    year1 = None
    year2 = None
    wu1 =  None
    wu2 =  None
    diff = None
    if request.method == "POST":
        selected_name = request.form.get("country", "")
        year1_value = request.form.get("year1", "")
        year2_value = request.form.get("year2", "")
        if not selected_name:
            error = "Select a country to view its water usage data."
        elif not year1_value or not year2_value:
            error = "Select years to view its water usage data."
        else:
            try:
                year1 = int(year1_value)
                year2 = int(year2_value)
                compare_out = water_use_time_compare(selected_name, year1, year2)
                wu1 = round(float(compare_out[3]) ,2)
                wu2 = round(float(compare_out[4]) ,2)
                diff = str(round(float(wu2) - float(wu1),2))
            except (ValueError, IndexError):
                error = "Invalid country or year selection."


    return render_template(
        "compare.html",
        names=names,
        selected_name=selected_name,
        error=error,
        year1=year1,
        year2=year2,
        water_use_year1 = wu1,
        water_use_year2 = wu2,
        difference = diff
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
    print(e)
    return render_template("404.html"), 404

def main():
    """Main function to run the Flask app."""
    app.register_blueprint(api, url_prefix='/api')
    app.run(host="0.0.0.0", port=5310)
if __name__ == '__main__':
    main()
