## Connect to database/log file

from sqlite3 import connect
import random
import datetime


class access:
    ## Defines methods to access quotes from the json file
    def getQuotesRan(category) -> tuple:
        ## Method returns a random quote from the given category as a tuple
        quotes = connect('quotes_database.db')

        try:
            ## Try to get all quotes from selected category
            catQuotes = quotes.execute(f"SELECT quote, author FROM {category}")
            catQuotes = catQuotes.fetchall()
            ## Get a list of all the categories in the json

            return random.choices(catQuotes)[0]

        except:
            ## Raises exception when category does not exist
            return "Category does not exist"

    def getQuotesLike(category) -> str:
        ## Returns a quote based on the number of likes
        quotes = connect('quotes_database.db')
        try:
            catQuotes = quotes.execute("SELECT quote FROM ?", (category,))
            ## Sort by likes

        except:
            return "Category does not exist"

    def getLength(category) -> int:
        ## Returns the number of quotes in the given category
        quotes =  connect('quotes_database.db')
        try:
            catQuotes.execute(f"SELECT quote FROM {category}")
            catQuotes = catQuotes.fetchall()
            return len(catQuotes)

        except:
            return "Category does not exist"


class append:
    ## Defines methods to edit quotes in the json file
    def addQuotes(category, quote, author):
        ## This method adds quotes to existing categories, returns True if successful, False if fails
        quotes = connect("quotes_database.db")
        try:
            date = datetime.datetime.today().strftime("%Y-%m-%d")
            quotes.execute("INSERT INTO ? VALUES (?,?,?)",(category, quote, author, date,))
            quotes.commit()
            quotes.close()
            return True

        except:
            quotes.close()
            return "Category does not exist"

    def addCat(category):
        ## This method adds a new category to the database
        ## Adds a new category ONLY, this method does not add any quotes
        try:
            quotes = connect("quotes_database.db")
            quotes.execute("CREATE TABLE ?(quote TEXT, author TEXT, date, TEXT)", (category,))
            return True

        except:
            return False
