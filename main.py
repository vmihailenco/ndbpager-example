from google.appengine.ext.webapp.util import run_wsgi_app

from app import app


def main():
    run_wsgi_app(app)


if __name__ == '__main__':
    main()
