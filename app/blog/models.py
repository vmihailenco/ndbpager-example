from google.appengine.ext import ndb


class Article(ndb.Model):
    title = ndb.StringProperty(required=True)
    text = ndb.TextProperty(required=True)
