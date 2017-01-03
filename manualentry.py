from pyteaser import SummarizeUrl

############## SUMMARIZER ##################

while True:

	corpurl = input('Please paste in the URL of your choice! It will be summarized and placed into corpus.txt')

	summary = str(SummarizeUrl(corpurl)) # summarizes

	mprint = open ('corpus.txt', 'w') 
	mprint.write (summary) # writes summaries to Markov Corpus



	

	


