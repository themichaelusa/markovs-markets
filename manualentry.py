import newspaper 
from newspaper import Article
############## SUMMARIZER ##################

while True:

	corpurl = raw_input('Please paste in the URL of your choice! It will be summarized and placed into corpus.txt')

	a = Article(corpurl, language='en') 
	a.download()
	a.parse()
	a.nlp()
	
	summsend = str(a.summary) # summarizes
	print(summsend)

	mprint = open ('corpus.txt', 'a') 
	mprint.write (summsend) # writes summaries to Markov Corpus



	

	


