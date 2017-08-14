#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import jinja2
import webapp2
import os
import unirest
import time
from google.appengine.api import urlfetch


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        # url = 'https://api.themoviedb.org/3/movie/10016?api_key=908b04b14312a6971d28a297db411fd7&language=en-US'
        # try:
        #     result = urlfetch.fetch(url)
        #     if result.status_code == 200:
        #         self.response.write(result)
        #     else:
        #         self.response.status_code = result.status_code
        # except urlfetch.Error:
        #     logging.exception('Caught exception fetching url')

        def callback(response):
            print(str(response.body))
            self.response.write(response.body)

        params = {'api_key': '908b04b14312a6971d28a297db411fd7'}
        url = 'https://api.themoviedb.org/3/movie/10016?&language=en-US'

        response = unirest.get(url, params = params, callback = callback)
        time.sleep(1)
        # self.response.write(m)


        #

        template = env.get_template('home.html')
        vars = {'CompanyName': 'louis.lewis movies'}
        # self.response.out.write(template.render(vars))
        # self.response.write()

class GenreHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('genre.html')
        self.response.out.write(template.render())

class ReviewsHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('reviewsform.html')
        self.response.out.write(template.render())

class CastHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('cast.html')
        self.response.out.write(template.render())

class OtherMoviesHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('othermovies.html')
        self.response.out.write(template.render())
class RatingHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('rating.html')
        self.response.out.write(template.render())

class DirectorHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('director.html')
        self.response.out.write(template.render())

class StyleHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('style.html')
        self.response.out.write(template.render())

class RecHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('recommendations.html')
        self.response.out.write(template.render({self.request.get('genre')}))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    # ('/login', UserHandler),
    ('/genre', GenreHandler),
    ('/reviews', ReviewsHandler),
    ('/cast', CastHandler),
    ('/othermovies', OtherMoviesHandler),
    ('/rating', RatingHandler),
    ('/director', DirectorHandler),
    ('/style', StyleHandler),
    ('/recommendations', RecHandler)
], debug=True)
