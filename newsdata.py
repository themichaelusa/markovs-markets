import newspaper 
from pyteaser import SummarizeUrl
# from newspaper import news_pool

############## NEWSPAPER ##################

newspaper.languages()

marketwatch = newspaper.build('http://www.marketwatch.com')

# bloomberg = newspaper.build('https://www.bloomberg.com')
# cnbc = newspaper.build('http://www.cnbc.com')
# gfin = newspaper.build('https://www.google.com/finance')

# news = [marketwatch, bloomberg, cnbc, gfin]
# news_pool.set(news, threads_per_source=2) # 8 threads 
# news_pool.join()

while True:

	corpurl = ''

	for article in marketwatch.articles:
		marketwatch.size()
		corpurl = article.url

	summary = str(SummarizeUrl(corpurl))

	mprint = open ('corpus.txt', 'a') #append tag
	mprint.write (summary) # writes summaries to Markov Corpus


	

	


