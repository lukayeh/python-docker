import os
import socket
import sys
import json
import pwd

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant


# a simple pay that says hello
@app.route("/")
def hello():
    html = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>Python:</b> {version}<br/>"
        "<b>User:</b> {user}<br/>"
    )
    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        version=sys.version,
        user=pwd.getpwuid(os.getuid())[0],
    )


@app.route("/json")
def json():
    data = jsonify(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        python_version=sys.version,
        user=pwd.getpwuid(os.getuid())[0],
        status=200,
        mimetype="application/json",
    )
    return data
