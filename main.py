# app.py
import reader
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Sample database code below
# Replace this with your database connection logic
quotes_database = {
    'motivation': ['Motivation quote 1', 'Motivation quote 2', 'Motivation quote 3'],
    # Add entries for other topics
}

@app.route('/')
def index():
    return render_template('quotes.html')   

@app.route('/random/<topic>')
def random_quote(topic):
    # Logic to get a random quote for the specified topic
    # Replace this with your actual logic to select a random quote
    random_quote = reader.access.getQuotesRan(topic)
    return render_template('listofquotes.html', random_quote=random_quote, topic=topic)

@app.route('/home')
def home():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
