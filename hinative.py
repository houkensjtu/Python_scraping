from urllib2 import urlopen
from urllib2 import URLError
from bs4 import BeautifulSoup
from time import sleep
import requests

# proxies will only be necessary when you are behind an evil firewall...
proxies = {'http':'http://ch40203515%40shi-g.com:2N%21n9Ly%24\
          @tnsproxy.shi.co.jp:8080','https':'http://ch4020351\
          5%40shi-g.com:2N%21n9Ly%24@tnsproxy.shi.co.jp:8080'}

# Get the target page by urlopen, return a html object.
def getHtmlUrlopen(url):
    try:
        html = urlopen(url)
    # In order to handle HTTP error.   
    except URLError as e:
        print(e)
    else:
        return html

# Get the token by urlopen, return the token.
def getTokenUrlopen(html):
    bsobj = BeautifulSoup(html.read(),"html.parser")
    token = bsobj.find("meta",{"name":"csrf-token"})['content']
    print("Your token is: %s" %token)
    return token

# Get the token by Requests(module), return the token.
def getTokenRequests(session):
     response = session.get('https://hinative.com/en-US/users/sign_in')
     bsobj = BeautifulSoup(response.text,"html.parser")
     token = bsobj.find("meta",{"name":"csrf-token"})['content']
     print("Your token is: %s" %token)
     return token

# Get the user's ID from "setting" page, need a Requests session as argument. 
def getUserID(session):
    response = session.get('https://hinative.com/en-US/setting')
    bsobj = BeautifulSoup(response.text,"html.parser")
    userID = bsobj.find("div",{"class":"container js-wrapper"})['data-user-id']
    print("Your userID at \"HiNative.com\" is:"+userID)
    return userID

# Open a Requests session
session = requests.Session()

# Grab the token from response
token=getTokenRequests(session)

# Post the username, password and token to login
username = raw_input('Your username: ')
password = raw_input('Your password: ')
params={'user[login]':username,'user[password]':password\
        ,'authenticity_token':token,'user[remember_me]':0,\
        'user[remember_me]':1,'commit':'Sign in'}

loginPage = session.post('https://hinative.com/en-US/users/sign_in',params=params)
print("You are logged in!")

# Go to ask a question!
questionType = session.get('https://hinative.com/en-US/questions/type')
print(questionType.text)
bsobj = BeautifulSoup(questionType.text,"html.parser")
