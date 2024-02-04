## Connect to database/log file

import json
import random

raw = open('quotes.json', 'r+')
quotes = json.load(raw)
raw.close()

class access:
    ## Defines methods to access quotes from the json file
    def getQuotesRan(category) -> str:
        ## Returns a random quote from the given category
        cats = list(quotes.keys())
        ## Get a list of all the categories in the json

        if not category in cats:
            return "Category does not exist"

        else:
            catQuotes = quotes[category]
            return random.choices(catQuotes) 

    def getQuotesLik(category) -> str:
        ## Returns a quote based on the number of likes
        cats = list(quotes.keys())

        if not category in cats:
            return "Category does not exist"

        else:
            catQuotes = quotes[category]


class append:
    ## Defines methods to edit quotes in the json file
    def addQuotes(category, quote) -> bool:
        ## This method adds quotes to existing categories, returns True if successful, False if fails
        cats = list(quotes.keys())
        if not category in cats:
            return False

        else:
            quotes[category].append(quote)

            raw = open('quotes.json', 'r+')
            json.dump(quotes, raw, indent = 2)
            raw.close()
            return True

    def addCat(category) -> bool:
        ## Method adds a new category to the json file, returns True if successful, False if the category already exists
        cats = list(quotes.keys())
        if not category in cats:
            newCat = {category: []}
            ## Add an empty array to the new category
            quotes.update(newCat)

            raw = open("quotes.json", 'r+')
            json.dump(quotes, raw, indent=2)
            raw.close()

            return True

        else:
            return False


test = access()
test.getQuotes("Family")