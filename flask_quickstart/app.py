from logging.config import dictConfig

from flask import (Flask, abort, flash, make_response, redirect,
                   render_template, request, session, url_for)
from markupsafe import escape

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "WARNING", "handlers": ["wsgi"]},
    }
)


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def valid_login(username: str, password: str) -> None:
    ...


def log_the_user_in(username: str) -> None:
    ...


@app.route("/")
def index():
    # username = request.cookies.get('username')
    return redirect(url_for("login"))


@app.route("/hello")
@app.route("/hello/<name>")
def hello_world(name=None):
    return render_template("index.html", name=name)


# @app.route("/<name>")
# def hello_user(name):
#     return f"Hello, {escape(name)}!"


@app.route("/user/<username>")
def show_user_profile(username):
    # show the user profile for that user
    # app.logger.warning(username)

    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


@app.route("/projects/")
def projects():
    return "The project page"


@app.route("/about")
def about():
    return "The about page"


# =========
@app.route("/login", methods=["GET", "POST"])
def login():
    # abort(401)
    error = None
    if request.method == "POST":
        if valid_login(request.form["username"], request.form["password"]):
            return log_the_user_in(request.form["username"])
        else:
            flash("Invalid password provided", "error")
            error = "Invalid username/password"

    search_word = request.args.get("key", "")
    # the code below is executed if the request method
    # was GET or the credentials were invalid

    return render_template("login.html", error=error)


# ========= alternative way
# @app.get("/login")
# def login_get():
#     return show_the_login_form()


# @app.post("/login")
# def login_post():
#     return do_the_login()


# =========


@app.route("/user/<username>")
def profile(username):
    return f"{username}'s profile"


with app.test_request_context():
    # print(url_for("index"))
    # print(url_for("login"))
    # print(url_for("login", next="/"))
    # print(url_for("profile", username="John Doe"))

    url_for("static", filename="style.css")


@app.route("/upload", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["the_file"]
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template("page_not_found.html"), 404)
    resp.set_cookie("username", "the username")

    resp.headers["X-Something"] = "A value"
    return resp


@app.route("/logout")
def logout():
    # remove the username from the session if it's there
    session.pop("username", None)
    return redirect(url_for("index"))


# app.run(debug=True, use_debugger=False, use_reloader=False)
