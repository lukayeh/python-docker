import os
import socket
import sys
import json
import pwd

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from os.path import dirname

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant

with open(dirname(__file__) + '/pkg_info.json') as fp:
    info = json.load(fp)

__version__ = info['version']

# a simple pay that says hello
@app.route("/")
def hello():
    html = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>Python:</b> {pyversion}<br/>"
        "<b>User:</b> {user}<br/>"
        "<b>Version:</b> {version}<br/>"
    )
    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        pyversion=sys.version,
        version=__version__,
        user=pwd.getpwuid(os.getuid())[0],
    )

@app.route("/json")
def json():
    data = jsonify(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        python_version=sys.version,
        user=pwd.getpwuid(os.getuid())[0],
        version=__version__,
        status=200,
        mimetype="application/json",
    )
    return data
