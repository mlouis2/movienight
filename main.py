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
from watch import User
from watch import Watch
from google.appengine.api import urlfetch
from datetime import datetime, date
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):

        def callback(response):
            print(str(response.body))
            self.response.write(response.body)

        params = {'api_key': '908b04b14312a6971d28a297db411fd7'}
        url = 'https://api.themoviedb.org/3/movie/10016?&language=en-US'

        response = unirest.get(url, params = params, callback = callback)
        time.sleep(1)

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')

        user = users.get_current_user()
        if user:
            u = User.query(User.email == user.email()).get()
            if u:
                pass
            else:
                user_object = User(
                    email= user.email(),
                    history= [],
                )
                user_object.put()

        self.response.out.write(template.render())

class UserHandler (webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('<a href="%s">Are you sure you want to sign out?</a>' %
                (users.create_logout_url('/')))

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
                'genre': genre,
                'adult':adult
            }
        self.response.out.write(template.render(vars))

class ReviewsHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('reviewsform.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        year = self.request.get('year')
        vars = {
            'genre': genre,
            'adult':adult,
            'year': year
        }
        self.response.out.write(template.render(vars))

class CompaniesHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('Companies.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        year = self.request.get('year')
        vars = {
            'genre': genre,
            'adult':adult,
            'year': year
            }
        self.response.out.write(template.render(vars))

class RuntimeHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('runtime.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        year = self.request.get('year')
        company = self.request.get('company')
        vars = {
            'genre': genre,
            'adult':adult,
            'year': year,
            'company': company
            }
        self.response.out.write(template.render(vars))

class CastHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('cast.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        year = self.request.get('year')
        company = self.request.get('company')
        vars = {
            'genre': genre,
            'adult':adult,
            'year': year,
            'company': company
            }
        self.response.out.write(template.render(vars))

class RecHandler(webapp2.RequestHandler):
    def post(self):
        template = env.get_template('recommendations.html')
        genre = self.request.get('genre')
        adult = self.request.get('adult')
        year = self.request.get('year')
        company = self.request.get('company')
        runtime = self.request.get('runtime')

        def callback(response):
            print(str(response.body))
            movies = []
            movieposters = []
            # self.response.write(movies)
            for movie in response.body['results']:
                movieposters.append(movie['poster_path'])
                if movie['poster_path']:
                    movies.append({
                        'url': "https://image.tmdb.org/t/p/w300/" + movie['poster_path'],
                        'title': clean(movie['title']),
                        'overview': clean(movie['overview']),
                        'movie_id': movie['id']
                    })
            vars = {
                'genre': genre,
                'adult': adult,
                'year': year,
                'movies': movies,
                'movieposters': movieposters,
                'company': company,
            }

            if len(movies) > 0:
                vars['results'] = ''
                self.response.out.write(template.render(vars))
            else:
                vars['results'] = 'Sorry, no results for those parameters! Please try again.'
                self.response.out.write(template.render(vars))

        base_url = 'https://api.themoviedb.org/3/discover/movie'

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
            'ScienceFiction': 878,
            'TVMovie': 10770,
            'Thriller': 53,
            'War': 10752,
            'Western': 37
        }

        companies = {
            'Disney': 2,
            'Paramount': 4,
            'Pixar': 3,
            'NewLineCinema': 12,
            'WarnerBros': 6194,
            'Fox': 306
        }

        new = date(2016, 1, 1)
        recent = date(2007, 1, 1)
        old = date(2006, 1, 1)

        params = {'api_key': '908b04b14312a6971d28a297db411fd7', 'certification_country': 'US'}

        if self.request.get('genre') != '' and self.request.get('genre') != 'Any':
            params['with_genres'] = genres[self.request.get('genre')]

        if self.request.get('adult') == 'G':
            params['certification'] = 'G'
        elif self.request.get('adult') == 'PG':
            params['certification'] = 'PG'
        elif self.request.get('adult') == 'PG-13':
            params['certification'] = 'PG-13'
        elif self.request.get('adult') == 'R':
            params['certification'] = 'R'

        if self.request.get('year') == 'new':
            params['primary_release_date.gte'] = new
        elif self.request.get('year') == 'recent':
            params['primary_release_date.gte'] = recent
        elif self.request.get('year') == 'old':
            params['primary_release_date.lte'] = old

        if self.request.get('runtime') == 'long':
            params['with_runtime.gte'] = 120
        elif self.request.get('runtime') == 'medium':
            params['with_runtime.gte'] = 60
            params['with_runtime.lte'] = 120
        elif self.request.get('runtime') == 'short':
            params['with_runtime.lte'] = 60

        if company != 'Any' and company != '':
            params['with_companies'] = companies[self.request.get('company')]

        response = unirest.get(base_url, params = params, callback = callback)
        time.sleep(1)

def clean(s):
    return s.replace("'", "&#39;")

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('history.html')
        # self.response.write(template.render())

        user = users.get_current_user().user_id()
        # user_query = User.query(User.email == user.email())
        # user_results = user_query.get()
        # self.response.write(user_results)

        q = Watch.query(Watch.user_id == user)
        results = q.fetch()

        # self.response.write(results)


        movie_ids = []
        movie_paths = []
        movie_list = []
        movies = []

        def callback(response):
            movie = response.body
            movies.append({
                'url': "https://image.tmdb.org/t/p/w300/" + movie['poster_path'],
                'title': clean(movie['title']),
                'overview': clean(movie['overview']),
                'movie_id': movie['id']
            })

        base_url = 'https://api.themoviedb.org/3/movie/'
        params = {'api_key': '908b04b14312a6971d28a297db411fd7'}


        for result in results:
            url = base_url + str(result.movie_id)
            response = unirest.get(url, params = params, callback = callback)

        time.sleep(1)
        vars = {
            'movies': movies
        }
        print(movies)
        self.response.out.write(template.render(vars))

    def post(self):
        print(self.request.get('type'))
        if self.request.get('type') == 'add':
            user_id = users.get_current_user().user_id()
            movie_id = int(self.request.get('val'))

            q = Watch.query(Watch.user_id == user_id)
            results = q.fetch()
            movieids = []
            exists = False
            for result in results:
                movieids.append(result.movie_id)

            for movieid in movieids:
                if movie_id == movieid:
                    exists = True

            if exists != True:
                Watch(user_id = user_id, movie_id = movie_id).put()
        elif self.request.get('type') == 'remove':
            user_id = users.get_current_user().user_id()
            movie_id = int(self.request.get('val'))
            watch = Watch.query(Watch.movie_id == movie_id, Watch.user_id == user_id).get()
            watch.key.delete()


app = webapp2.WSGIApplication([
    ('/test', MainHandler),
    ('/', HomeHandler),
    ('/genre', GenreHandler),
    ('/adult', AdultHandler),
    ('/year', YearHandler),
    ('/companies', CompaniesHandler),
    ('/recommendations', RecHandler),
    ('/runtime', RuntimeHandler),
    ('/logout', UserHandler),
    ('/history', HistoryHandler)
], debug=True)
