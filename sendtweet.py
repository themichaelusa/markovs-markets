import os
import time
import twitter
from markovbot import MarkovBot

############## MARKOVBOT ##################

tweetbot = MarkovBot() # initializes Mbot instance

cons_key = ''
cons_secret = ''
access_token = ''
access_token_secret = ''

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret) #login

dirname = os.path.dirname(os.path.abspath(__file__)) # Get the current directory's path
corpread = os.path.join(dirname, 'corpus.txt') # Construct the path to the book
tweetbot.read(corpread) # reads corpus

sendout = tweetbot.generate_text(25) # generates tweet of 25 words
print (sendout)

tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=10, keywords=None, prefix=None)
time.sleep(600)




