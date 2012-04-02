from google.appengine.ext import ndb
import ndbpager
from flask import request, render_template

from . import blog
from .models import Article


@blog.route('/init/')
@ndb.toplevel
def article_init():
    for i in range(20):
        a = Article(title='article%d' % i, text='text%d' % i)
        a.put()
    raise ndb.Return('OK')


@blog.route('/')
@ndb.toplevel
def article_list():
    query = Article.query()
    pager = ndbpager.Pager(query=query, page=request.args.get('page', 1))
    articles, _, _ = pager.paginate(page_size=10)
    template_context = dict(
        articles=articles,
        pager=pager,
    )
    raise ndb.Return(
        render_template('blog/article_list.html', **template_context))
