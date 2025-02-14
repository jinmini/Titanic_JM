from flask import Flask, render_template, request, redirect, url_for
from com.jinmini.models.titanic.controller import Controller


app = Flask(__name__)

@app.route('/') 
def home():
    controller = Controller()
    controller.modeling("train.csv")
    return render_template("home.html")

@app.route('/taitanic_ml')
def taitanic_ml():
    return render_template("titanic_ml.html")

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True
