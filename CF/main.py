"""This module is called by Google App Engine

It looks for "app" in the "main.py" class to run flask with gunicorn"""

from flask import Flask
from CF.app.api import v1, v2, v3


app = Flask(__name__)
# app.register_blueprint(v1)  # original version
app.register_blueprint(v2)  # new version
# app.register_blueprint(v3)  # db version

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google app
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # app Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=5000, debug=True)
