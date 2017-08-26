import os
from flask import Flask,render_template,Blueprint
# from flask_cors import *
from app.chart import chart
from app.contract import contract
from app.BSmodule import BSmodule
from app.tools import tools
import chartkick

app = Flask(__name__, static_url_path='')
# CORS(app, supports_credentials=True)
app.debug = True

DATABASE_URL = os.path.realpath('./db/contract.db')

app.register_blueprint(contract, url_prefix='/contract')
app.register_blueprint(chart, url_prefix='/chart')
app.register_blueprint(BSmodule, url_prefix='/BSmodule')
app.register_blueprint(tools, url_prefix='/tools')
app.jinja_env.add_extension("chartkick.ext.charts")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    app.run()