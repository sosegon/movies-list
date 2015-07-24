#!/usr/bin/python

# basic code from http://learnpythonthehardway.org/book/ex50.html

import web
from movies.entertainment_center import *

urls = (
	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index():
	def GET(self):
		movies = read_movies_file("static/list.json")
		return render.index(movies)

if __name__ == "__main__":
	app.run()