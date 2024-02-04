## Connect to database/log file

from sqlite3 import connect
import random
import datetime


class access:
    ## Defines methods to access quotes from the json file
    quotes = connect('quotes_database.db')

    def getQuotesRan(category) -> str:
        ## Method returns a random quote from the given category
        try:
            ## Try to get all quotes from selected category
            catQuotes = quotes.execute("SELECT quote, author FROM ?", (category,))
            ## Get a list of all the categories in the json

            return random.choices(catQuotes)

        except:
            ## Raises exception when category does not exist
            return "Category does not exist"

    def getQuotesLike(category) -> str:
        ## Returns a quote based on the number of likes
        try:
            catQuotes = quotes.execute("SELECT quote FROM ?", (category,))



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

test = access()
test.getQuotes("Family")