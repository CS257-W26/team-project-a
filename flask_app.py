'''
The location for the Flask app interface for the project.
'''

from flask import Flask, Blueprint
from ProductionCode.use_time_compare import water_use_time_compare
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.per_capita import print_per_capita_water_use
from ProductionCode.database import open_database, id_to_db

app = Flask(__name__)
api = Blueprint('api', __name__)

@app.route('/')
def home():
    '''Home route'''
    return "Welcome to the Global Water Sources v Spending website!"

@app.route('/water_use/<country>/<year1>/<year2>/')
def water_use_route(country, year1, year2):
    """Route for water use."""
    try:
        result = water_use_time_compare(country, year1, year2)
        return result
    except ValueError as e:
        return str(e)


@app.route('/usage_proportion/<country>/<year>/')
def usage_proportion_route(country, year):
    '''Usage proportion route'''
    try:
        result = usage_proportion(country, year)
        return result
    except ValueError as e:
        return str(e)

@app.route('/per_capita/<country>/<year>/')
def per_capita_route(country, year):
    '''Per capita water use route'''
    try:
        value = print_per_capita_water_use(country, year)
        return value
    except ValueError as e:
        return str(e)

@api.route('/<int:database_id>/<int:row>/')
def get_database_row(database_id,row):
    """API route for directly accessing the database."""
    try:
        value = open_database(id_to_db(database_id))[row]
        return value
    except IndexError:
        return "Could not find the requested row or database. Valid database ids are 0-4 inclusive."

@app.errorhandler(404)
def page_not_found(e):
    '''Handle 404 errors'''
    return "Page not found. Try re-entering the link. Error: " + str(e)


if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(port = 5000)
