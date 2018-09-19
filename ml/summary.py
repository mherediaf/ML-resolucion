import click
from flask.cli import with_appcontext

# from . import day_event
from day_event import getEventFromDay, getPrecipitation

# @click.command('get-summary')
# @with_appcontext
def get_summary_of_days():
	sequia = 0
	optimo = 0
	lluvia = 0
	periodos_optimos = 0
	periodos_lluvia = 0
	prev = 'nada'
	dia_max_lluvia = 0
	max_lluvia = -1
	for day in range(0, 3650+1):
		event = getEventFromDay(day)
		if (event == 'sequia'):
			sequia = sequia+1
		elif (event == "optimo"):
			optimo = optimo+1
			if (prev != event):
				periodos_optimos = periodos_optimos+1
		elif (event == "lluvia"):
			lluvia = lluvia+1
			precip = getPrecipitation(day)
			if (precip > max_lluvia):
				max_lluvia = precip
				dia_max_lluvia = day
			if (prev != event):
				periodos_lluvia = periodos_lluvia+1
		prev = event
	click.echo("Periodos de sequia: " + str(sequia))
	click.echo("Dias de condiciones optimas de presion y temperatura: " + str(optimo))
	click.echo("Periodos de condiciones optimas de presion y temperatura: " + str(periodos_optimos))
	click.echo("Dias de precipitacion: " + str(lluvia))
	click.echo("Periodos de precipitacion: " + str(periodos_lluvia))
	click.echo("Dia de pico maximo de precipitacion: " + str(dia_max_lluvia))

get_summary_of_days()