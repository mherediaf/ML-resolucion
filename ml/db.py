import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

from day_event import getEventFromDay

def get_db():
	if 'db' not in g:
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types=sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row
	return g.db

def close_db(e=None):
	db = g.pop('db', None)
	if db is not None:
		db.close()

def init_db():
	db = get_db()
	with current_app.open_resource('schema.sql') as f:
		# print('aaa')
		db.executescript( f.read().decode('utf8') )


def load_data_for_every_day():
	for day in range(0, 3650+1):
		event = getEventFromDay(day)
		insertData(day, event)

def insertData(day, event):
	db = get_db()
	cursor = db.cursor()
	cursor.execute("INSERT INTO day_event VALUES (?, ?)", (day, event))

def loadEventForDayFromDb(day):
	db = get_db()
	cursor = db.cursor()
	cursor.execute("SELECT event FROM day_event WHERE day = ?", (day,))
	res = cursor.fetchone()
	# print(res)
	# return res
	return res['event']
	# return res[0]

@click.command('init-db')
@with_appcontext
def init_db_command():
	"""Clear the existing data and create new tables."""
	init_db()
	load_data_for_every_day()
	click.echo('Initialized the database.')

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)
