import os
import time
import twitter
from markovbot import MarkovBot

############## MARKOVBOT ##################

tweetbot = MarkovBot() # initializes Mbot instance

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret) #login

dirname = os.path.dirname(os.path.abspath(__file__)) # Get the current directory's path
corpread = os.path.join(dirname, 'corpus.txt') # Construct the path to the book
tweetbot.read(corpread)

while True: 
	sendout = tweetbot.generate_text(20) # tweet of 20 words
	tweetbot.twitter_tweeting_start(days=0, hours=, minutes=10, keywords=None, prefix=None, suffix='#MAGA')
	# time.sleep(600)




