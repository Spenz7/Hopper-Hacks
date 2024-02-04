
import reader
import random
import flask, sqlite3
from flask import render_template,request, jsonify

app = flask.Flask(__name__)

#sample database code below
#quote index is quote no.
quotes_database = {'topic':[{'quote index':'quote itself','likes':0}]}

@app.route('/')
def quotes():
    return render_template('quotes.html')

if __name__ == '__main__':
    app.run()






