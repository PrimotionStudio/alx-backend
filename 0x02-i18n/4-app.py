#!/usr/bin/env python3
"""
setup a basic flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    class to configure babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    get the locale from the user
    """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    display the index page
    """
    return render_template('4-index.html', locale=get_locale())


if __name__ == "__main__":
    app.run()
