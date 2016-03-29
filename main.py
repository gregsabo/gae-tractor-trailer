#!/usr/bin/env python

import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def template(name):
    return JINJA_ENVIRONMENT.get_template(name + '.html')


class TractorHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(template('tractor').render())


class TrailerHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(template('trailer').render())


app = webapp2.WSGIApplication([
    ('/', TractorHandler),
    ('/trailer', TrailerHandler),
    ('/tractor', TractorHandler),
], debug=True)
