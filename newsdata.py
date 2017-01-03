import newspaper 
# from newspaper import news_pool

############## NEWSPAPER ##################

marketwatch = newspaper.build('http://www.marketwatch.com')

# bloomberg = newspaper.build('https://www.bloomberg.com')
# cnbc = newspaper.build('http://www.cnbc.com')
# gfin = newspaper.build('https://www.google.com/finance')

# news = [marketwatch, bloomberg, cnbc, gfin]
# news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
# news_pool.join()

while True: 

	for article in marketwatch.articles: # gets recent articles && checks for dupes
		marketwatch.size()

	mainarticle = marketwatch.articles[0] # referencing market watch as source
	mainarticle.download() # gets most recent article
	mainarticle.parse() # parses text from article
	mainarticle.nlp() # preps for extracting summary

	mprint = open (corpus.txt, 'w') 
	mprint.write (mainarticle.summary + "/n") # writes summaries to Markov Corpus

	


