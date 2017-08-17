from google.appengine.ext import ndb

class Watch (ndb.Model):
    user_id = ndb.StringProperty()
    movie_id = ndb.IntegerProperty()

class User (ndb.Model):
    email = ndb.StringProperty()
    history = ndb.StringProperty(repeated = True)
