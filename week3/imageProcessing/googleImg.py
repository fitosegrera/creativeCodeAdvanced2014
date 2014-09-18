import urllib2
import simplejson
import urllib
import os

from generativeImg import generativeImg
imageGen = generativeImg()

class googleImg:

	def searchAndDownload(self, q):
		numOfImgs = 10
		urls = []

		url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=barack%20obama&userip=INSERT-USER-IP')

		searchTerm = q
		os.makedirs(searchTerm)

		request = urllib2.Request(url)
		response = urllib2.urlopen(request)

		# Set count to 0
		count= 0

		for i in range(0,numOfImgs):
		    #request a new set of images for each loop
		    url = ('https://ajax.googleapis.com/ajax/services/search/images?' + 'v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
		    print url
		    request = urllib2.Request(url, None, {'Referer': 'testing'})
		    response = urllib2.urlopen(request)

		    # Get the complete JSON
		    results = simplejson.load(response)
		    data = results['responseData']
		    dataInfo = data['results']

		    # Iterate for each result and get the element unescaped url from the JSON
		    for myUrl in dataInfo:
		        print myUrl['unescapedUrl']
		        image = urllib.URLopener()
		        image.retrieve(myUrl['unescapedUrl'], searchTerm+"/"+str(count)+".jpg")
		        urls.append(searchTerm+"/"+str(count)+".jpg" )
		        count = count + 1

		imageGen.generate(urls, searchTerm)  