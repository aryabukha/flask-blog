from flask import Flask
from src.handlers.hello import hello_world


app = Flask(__name__)


app.add_url_rule("/hello/<name>", "hello", hello_world, methods=["GET", "POST"])
