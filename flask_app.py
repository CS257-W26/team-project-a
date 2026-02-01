'''
The location for the Flask app interface for the project.
'''

from flask import Flask, Blueprint 
from ProductionCode.use_time_compare import water_use_time_compare
from ProductionCode.usage_proportion import usage_proportion
from ProductionCode.per_capita import print_per_capita_water_use

app = Flask(__name__)
api = Blueprint('api', __name__)

@app.route('/')
def home():
    '''Home route'''
    return "Welcome to the Global Water Sources v Spending website!"

@app.route('/water_use/<country>/<year1>/<year2>')
def water_use_route(country, year1, year2):
    try:
        result = water_use_time_compare(country, year1, year2)
        return result
    except ValueError as e:
        return str(e)


@app.route('/usage_proportion/<country>/<year>')
def usage_proportion_route(country, year):
    '''Usage proportion route'''
    try:
        result = usage_proportion(country, year)
        return result
    except ValueError as e:
        return str(e)

@app.route('/per_capita/<country>/<year>')
def per_capita_route(country, year):
    '''Per capita water use route'''
    try:
        value = print_per_capita_water_use(country, year)
        return value
    except ValueError as e:
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    '''Handle 404 errors'''
    return "Page not found", 404


if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(port = 5000)