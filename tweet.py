import newspaper 
import markovify
# from newspaper import news_pool

############## NEWSPAPER ##################

marketwatch = newspaper.build('http://www.marketwatch.com')

# bloomberg = newspaper.build('https://www.bloomberg.com')
# cnbc = newspaper.build('http://www.cnbc.com')
# gfin = newspaper.build('https://www.google.com/finance')

# news = [marketwatch, bloomberg, cnbc, gfin]
# news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
# news_pool.join()

for article in marketwatch.articles: # gets recent articles && checks for dupes
	print (article.url)
	marketwatch.size()

mainarticle = marketwatch.articles[0] # referencing market watch as source
mainarticle.download() # gets most recent article
mainarticle.parse() # parses text from article
mainarticle.nlp() # preps for extracting summary

mprint = open (corpus.txt, 'w')
mprint.write (mainarticle.summary)

############## MARKOVIFY ##################

with open ("/Users/michaelusa/Documents/Dev/markovs-markets/corpus.txt") as r:
	text = r.read()

model = markovify.Text(text)
m2print = open (outbound.txt, 'w')

for i in range(3):
	m2print.write (model.make_short_sentence(140))






