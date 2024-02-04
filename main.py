# app.py
import reader
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)



@app.route('/')
def index():
    oldquotes = []
    return render_template('quotes.html')   

oldquotes = []

@app.route('/random/<topic>')
def random_quote(topic):
    # Logic to get a random quote for the specified topic
    # Replace this with your actual logic to select a random quote
    if len(oldquotes) == reader.access.getLength(topic):
        newquote = 'There are no more quotes'
        return render_template('listofquotes.html', random_quote=newquote, topic=topic)

    newquote = reader.access.getQuotesRan(topic)
    while newquote[0] in oldquotes: #2nd time onwards
        newquote = reader.access.getQuotesRan(topic)
    oldquotes.append(newquote[0])
    newquote = newquote[0] + ' - ' + newquote[1]
    return render_template('listofquotes.html', random_quote=newquote, topic=topic)

@app.route('/home')
def home():
    while len(oldquotes)!=0:
        oldquotes.pop()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()