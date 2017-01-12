import sys
import nltk
import newspaper 
from newspaper import Article
# from newspaper import news_pool

############## NEWSPAPER ##################

newspaper.languages()

marketwatch = newspaper.build(u'http://www.marketwatch.com', language = 'en')

# bloomberg = newspaper.build('https://www.bloomberg.com')
# cnbc = newspaper.build('http://www.cnbc.com')
# gfin = newspaper.build('https://www.google.com/finance')

# news = [marketwatch, bloomberg, cnbc, gfin]
# news_pool.set(news, threads_per_source=2) # 8 threads 
# news_pool.join()

while True:

	reload(sys)
	sys.setdefaultencoding('utf-8')

	marketwatch.size() # updates total size on first run

	if (marketwatch.size() > 0):
		articlemw = marketwatch.articles[0]
		articlemw.download()
		articlemw.parse()
		articlemw.nlp()
		pushsummary = str(articlemw.summary) # str fixes ascii issue
		print (pushsummary) # nice readout in terminal
		mprint = open ('corpus.txt', 'a') #append tag
		mprint.write (pushsummary) # writes summaries to Markov Corpus
	
	


	

	


