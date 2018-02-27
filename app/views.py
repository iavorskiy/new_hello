from flask import render_template
import socket
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/test')
def test():
    docker_id = socket.gethostname()
    return docker_id
