#!/usr/bin/env python3
"""
setup a basic flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    get user from session
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    function to get user locale and timezone
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    get the locale from the user
    """
    locale = request.args.get('locale')
    if locale in app.config["LANGUAGES"]:
        return locale
    user = getattr(g, "user", None)
    if user and user["locale"] in app.config["LANGUAGES"]:
        return user["locale"]
    loc = request.accept_languages.best_match(app.config["LANGUAGES"])
    if loc:
        return loc
    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """
    Get the timezone from the user
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    user = getattr(g, 'user', None)
    if user:
        try:
            return pytz.timezone(user['timezone']).zone
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/")
def index():
    """
    display the index page
    """
    return render_template('7-index.html', locale=get_locale())


if __name__ == "__main__":
    app.run()
