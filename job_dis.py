import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer

texts = []
# hold our job descriptions in this list
for index in range(0,1000,10): # go through 100 pages of indeed
    page = 'indeed.com/jobs?q=data+scientist&start='+str(index)
    # identify the url of the job listings
    web_result = requests.get(page).text
    # use requests to actually visit the url
    soup = BeautifulSoup(web_result)
    # parse the html of the resulting page
    for listing in soup.findAll('span', {'class':'summary'}):
    # for each listing on the page
        texts.append(listing.text)
    # append the text of the listing to our list

vect = CountVectorizer(ngram_range=(1,2), stop_words='english')
# Get basic counts of one and two word phrases
matrix = vect.fit_transform(texts)
# fit and learn to the vocabulary in the corpus
print(len(vect.get_feature_names())) # how many features are there
# There are 11,293 total one and two words phrases in my case!!