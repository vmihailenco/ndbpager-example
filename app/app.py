from flask import Flask


app = Flask(__name__)


from blog import blog
app.register_blueprint(blog)
