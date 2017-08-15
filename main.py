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
import json
import urllib
import urllib2
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


        # self.response.out.write(template.render(vars))
        # self.response.write()


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')
        self.response.out.write(template.render())

class UserHandler (webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                users.create_login_url('/'))
        self.response.write('<html><body>%s</body></html>' % greeting)

class GenreHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('genre.html')
        self.response.out.write(template.render())

class AdultHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('rating.html')
        genre = self.request.get('genre')
        vars = {
            'genre': genre
        }
        self.response.out.write(template.render(vars))

class YearHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('year.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        vars = {
                'genre': genre, 'adult':adult
            }
        self.response.out.write(template.render(vars))

class ReviewsHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('reviewsform.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        vars = {
            'genre': genre, 'adult':adult
        }
        self.response.out.write(template.render(vars))

class CompaniesHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('companies.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        vars = {
            'genre': genre, 'adult':adult
        }
        self.response.out.write(template.render(vars))

class CastHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('cast.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        vars = {
            'genre': genre, 'adult':adult
        }
        self.response.out.write(template.render(vars))




class RecHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('recommendations.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        def callback(response):
            print(str(response.body))
            movies = []
            for movie in response.body['results']:

                movies.append(movie['title'])
               #self.response.write(movie['title'])
            vars = {
                'genre': genre,
                'adult': adult,
                'movies': movies
            }
            self.response.out.write(template.render(vars))
            #self.response.write(response.body['results'][0]['title'])

        base_url = 'https://api.themoviedb.org/3/discover/movie'

        #Dictionary of genres
        genres = {
            'Action': 28,
            'Adventure': 12,
            'Animation': 16,
            'Comedy': 35,
            'Crime': 80,
            'Documentary': 99,
            'Drama': 18,
            'Family': 10751,
            'Fantasy': 14,
            'History': 36,
            'Horror': 27,
            'Music': 10402,
            'Mystery': 9648,
            'Romance': 10749,
            'Science Fiction': 878,
            'TV Movie': 10770,
            'Thriller': 53,
            'War': 10752,
            'Western': 37
        }



        # if self.request.get('genre') not in genres.keys():
        #     self.response.write( self.request.get('genre'))
        # else:
        #     self.response.write( 'out' )
        #     self.response.write( self.request.get('genre'))

        if self.request.get('adult') == 'Adult':
            params = {'with_genres': genres[self.request.get('genre')], 'certification_country': 'US', 'certification': 'R', 'api_key': '908b04b14312a6971d28a297db411fd7', 'limit': 10}
        elif self.request.get('adult') == 'Kid':
            params = {'with_genres': genres[self.request.get('genre')],'certification_country': 'US', 'certification': 'G', 'api_key': '908b04b14312a6971d28a297db411fd7', 'limit': 10}
        else:
            params = {'with_genres': genres[self.request.get('genre')], 'api_key': '908b04b14312a6971d28a297db411fd7', 'limit': 10}
        response = unirest.get(base_url, params = params, callback = callback)
        time.sleep(1)

        # genre_rec = self.response.out.write(self.request.get('genre'))
        # self.response.out.write(template.render())



app = webapp2.WSGIApplication([
    ('/test', MainHandler),
    ('/', HomeHandler),
    ('/genre', GenreHandler),
    ('/adult', AdultHandler),
    ('/year', YearHandler),
    ('/reviews', ReviewsHandler),
    ('/companies', CompaniesHandler),
    ('/cast', CastHandler),
    ('/recommendations', RecHandler),
    ('/signup', UserHandler)
], debug=True)
