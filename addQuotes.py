import sqlite3
import json
from datetime import date

connection = sqlite3.connect("quotes_database.db")

quotesFile = open("quotes.json", "r")

with open("quotes.json", "r") as quotesFile:
    data = json.load(quotesFile)

motivation_quotes = data["Motivation"]
wisdom_quotes = data["Wisdom"]
family_quotes = data["Family"]
happiness_quotes = data["Happiness"]
pets_quotes = data["Pets"]

def add_quotes_to_table(table_name, quotes_list):
    for quote in quotes_list:
        cursor = connection.execute(
            f"SELECT COUNT(*) FROM {table_name} WHERE quote = ?",
            (quote["quote"],)
        )
        count = cursor.fetchone()[0]

        if count == 0:
            connection.execute(
                f"INSERT INTO {table_name} (quote, author, date) VALUES (?, ?, ?)",
                (quote["quote"], quote["author"], date.today())
            )
    
    connection.commit()

add_quotes_to_table("Motivation", motivation_quotes)
add_quotes_to_table("Wisdom", wisdom_quotes)
add_quotes_to_table("Family", family_quotes)
add_quotes_to_table("Happiness", happiness_quotes)
add_quotes_to_table("Pets", pets_quotes)


quotesFile.close()
