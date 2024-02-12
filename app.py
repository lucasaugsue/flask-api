from flask import Flask
from carros import carros_bp

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(carros_bp, url_prefix='/')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"