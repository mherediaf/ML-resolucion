import webapp2
from webapp2_extras import json
from day_event import getEventFromDay

class GetEventOfDayPage(webapp2.RequestHandler):
	def get(self):
		if (self.request.method == 'GET'):
			dia = self.request.GET['dia']
			self.response.headers['Content-Type'] = 'application/json'
			self.response.write(json.encode({'dia': dia, 'clima': getEventFromDay(dia)}))

app = webapp2.WSGIApplication([
	("/clima", GetEventOfDayPage)
], debug=True)