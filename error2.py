# A Python script to scrap the price of a certain Thinkpad model.

from urllib2 import urlopen
from urllib2 import URLError
from bs4 import BeautifulSoup

# Function for getting a specific url. Return a html object
def getHtml(url):
    try:
        html = urlopen(url)
        
    # In order to handle HTTP error.   
    except URLError as e:
        print(e)
    else:
        return html

# Function for extracting information from a html object.    
def getTitle(html):
     try:
         bsobj = BeautifulSoup(html.read(),"html.parser")
         # Find final price information by searching for following "class" attribute.
         title = bsobj(attrs= {"class","pricingSummary-details-final-price"})

     # If the attribute doesn't exist.
     except AttributeError as e:
         print("Required title not found...")
     else:
         if title is None:
             return None
         else:
             return title
# The following URL is the webshop page of Lenovo Japan for Thinkpad X1-carbon.
html = getHtml("http://shopap.lenovo.com/jp/notebooks/thinkpad/x-series/x1-carbon/")

# Print all the price information found on this page...
title = getTitle(html)
for line in title:
    print(line)
