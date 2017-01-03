import newspaper 
# from newspaper import news_pool
from pyteaser import SummarizeUrl

############## NEWSPAPER ##################
newspaper.languages()

# bloomberg = newspaper.build('https://www.bloomberg.com')
# cnbc = newspaper.build('http://www.cnbc.com')
# gfin = newspaper.build('https://www.google.com/finance')

# news = [marketwatch, bloomberg, cnbc, gfin]
# news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
# news_pool.join()

marketwatch = newspaper.build('http://www.marketwatch.com')

while True:

	corpurl = ''
	
	for article in marketwatch.articles:
		marketwatch.size()
		corpurl = article.url
		print(corpurl)

	summary = str(SummarizeUrl(corpurl))

	mprint = open ('corpus.txt', 'w') 
	mprint.write (summary) # writes summaries to Markov Corpus


	

	


