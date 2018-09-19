import os
import math
import click

from flask import Flask, abort, jsonify, request

from day_event import getEventFromDay
# from db import loadEventForDayFromDb
from summary import get_summary_of_days


def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	@app.route('/clima', methods=['GET'])
	def get_day():
		dia = request.args.get('dia', None)
		if dia is None:
			abort(404)
		return jsonify(dia=dia, clima=getEventFromDay(int(dia)))
		# Previous attempt. Using sqlite3
		# return jsonify(dia=dia, clima=loadEventForDayFromDb(dia))
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
	)
	# The following commented lines correspond to the previous attempt of using sqlite3
	# if test_config is None:
		# load the instance config, if it exists, when not testing
		# app.config.from_pyfile('config.py', silent=True)
	# else:
		# load the test config if passed in
		# app.config.from_mapping(test_config)
	# ensure the instance folder exists
	# try:
		# os.makedirs(app.instance_path)
	# except OSError:
		# pass
	# from . import db
	# db.init_app(app)
	return app
