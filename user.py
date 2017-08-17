from google.appengine.ext import ndb

class User (ndb.Model):
    email = ndb.StringProperty()
    history = ndb.StringProperty(repeated=True)
    age = ndb.IntegerProperty()
