import os
from flask import Flask
import socket
import sys

app = Flask(__name__)

# a simple pay that says hello
@app.route("/")
def hello():
    html = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>Python:</b> {version}<br/>"
    )
    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        version=sys.version,
    )
