import markovify
from twitter_markov import TwitterMarkov
import time

############## MARKOVIFY ##################

# with open ("/Users/michaelusa/Documents/Dev/markovs-markets/corpus.txt") as r:
#	text = r.read()

# model = markovify.Text(text) # uses corpus.txt as model for tweets
# m2print = open (outbound.txt, 'w')

# for i in range(1): 
# 	m2print.write (model.make_short_sentence(140) + "/n") #writes one tweet to outbound.txt plus newline


############## TWEET + MARKOVIFY ##################

while True: 
	sendtweet = TwitterMarkov('markovsmarkets', 'corpus.txt', config_file='bots.yaml')
	outbound = sendtweet.compose()
	time.sleep(600)


