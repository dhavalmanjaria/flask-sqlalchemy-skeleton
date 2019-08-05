from flask import (
    current_app as app,
    render_template,
    request,
    redirect,
    abort,
    url_for,
    session,
    Blueprint,
    Response,
    send_file,
)
from flask.helpers import safe_join
import os

cwd = os.getcwd()

views = Blueprint("views", __name__, template_folder="templates",
                  static_folder="static",
                  static_url_path="/static/")

@views.route("/", defaults={"route": "index"})
@views.route("/<path:route>")
def static_html(route):
    """
    Basic route
    :param route:
    :return:
    """

    return render_template('index.html')
