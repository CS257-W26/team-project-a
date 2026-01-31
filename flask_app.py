'''
The eventual location for the Flask app interface for the project.
'''

from flask import Flask, Blueprint 
from ProductionCode.database import DB, open_database, filter_tags_database
from ProductionCode.use_time_compare import water_use_time_compare, water_use_time_compare_print
from ProductionCode.usage_proportion import usage_proportion, get_usage_percentage
from ProductionCode.per_capita import get_per_capita_water_use

app = Flask(__name__)
api = Blueprint('api', __name__)

@app.route('/')
"""Home route"""
def home():
    return "Welcome to the Global Water Sources v Spending website!"


@app.route('/water_use/<country>/<year1>/<year2>')
"""Water use comparison route"""


@app.route('/usage_proportion/<country>/<year>')
"""Usage proportion route"""


@app.route('/per_capita/<country>/<year>')
"""Per capita water use route"""


@app.errorhandler(404)
"""404 error handler"""
def page_not_found(e):
    return "404 - Page Not Found", 404


if __name__ == '__main__':
    app.register_blueprint(api, url_prefix='/api')
    app.run(port = 5000)