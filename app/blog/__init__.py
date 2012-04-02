import urllib

from app import app
from flask import Blueprint, request


blog = Blueprint('blog', __name__, template_folder='templates')


from . import views


def url_for_other_page(page):
    args = request.args.copy()
    args['page'] = page
    return '?' + urllib.urlencode(args)


@app.context_processor
def inject():
    return dict(url_for_other_page=url_for_other_page)
