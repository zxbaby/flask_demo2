#coding:utf-8
from flask import Flask, render_template
from views.snscheduler import snscheduler
from flask_apscheduler import APScheduler
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
Bootstrap(app)
app.config.from_object('config')
app.register_blueprint(snscheduler)





@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
