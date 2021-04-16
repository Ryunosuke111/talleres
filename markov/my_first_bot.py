import os
from markovbot import MarkovBot



# Initialise a MarkovBot instance
print("-----------------------------------------------------------")
print("Initialising MarkovBot ...")
tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
print("-----------------------------")
print("Getting the path ...")
# Construct the path to the book
#book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
book = os.path.join(dirname, u'DonQuijote.txt')

# Make your bot read the book!
print("-----------------------------")
print("Reading the book ...")
#tweetbot.read(book)
tweetbot.read(book, database='_spanish')

print("-----------------------------")
print("Generating the text ...")
#my_first_text = tweetbot.generate_text(50, seedword=['dream', 'psychoanalysis'])
my_first_text = tweetbot.generate_text(50, database='_spanish', seedword=[u'Sancho', u'Rocinante'])
print("tweetbot says:")
print(my_first_text)
