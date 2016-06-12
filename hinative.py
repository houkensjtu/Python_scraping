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
def getTokenRequests(session,url):
     response = session.get(url)
     bsobj = BeautifulSoup(response.text,"html.parser")
     token = bsobj.find("meta",{"name":"csrf-token"})['content']
     print("Your token is: %s" %token)
     return token

# Get a token for asking question. (Asking question do need another token!)
def getAskTokenRequests(session,url):
     response = session.get(url)
     bsobj = BeautifulSoup(response.text,"html.parser")
     token = bsobj.find("input",{"name":"authenticity_token"})['value']
     print("Your token is: %s" %token)
     return token
 
# Get the user's ID from "setting" page, need a Requests session as argument. 
def getUserID(session):
    response = session.get('https://hinative.com/en-US/setting')
    bsobj = BeautifulSoup(response.text,"html.parser")
    userID = bsobj.find("div",{"class":"container js-wrapper"})['data-user-id']
    print("Your userID at \"HiNative.com\" is:"+userID)
    return userID

# 0.Prepare the URL will be used
loginUrl = 'https://hinative.com/en-US/users/sign_in'
askQuestionUrl = 'https://hinative.com/en-US/questions/type'

# 1.Open a Requests session
session = requests.Session()

# 2.Grab the token from response(for login)
token=getTokenRequests(session,loginUrl)

# 3.Post the username, password and token to login
username = raw_input('Your username: ')
password = raw_input('Your password: ')
params={'user[login]':username,'user[password]':password\
        ,'authenticity_token':token,'user[remember_me]':0,\
        'user[remember_me]':1,'commit':'Sign in'}

loginPage = session.post('https://hinative.com/en-US/users/sign_in',params=params)
print("You are logged in!")

# 4.Go to ask a question!

# Asking question need another token
token = getAskTokenRequests(session,'https://hinative.com/en-US/questions/new?type=WhatsayQuestion')

# 5.Although on Web you need to access 'https://hinative.com/en-US/questions/type' to select a type,
# the ultimate destination of that is, however, 'https://hinative.com/en-US/questions'.
questionContent = raw_input('Your question is: How do you say this in Japanese?')
params={'authenticity_token':token,'type':'WhatsayQuestion','question[language_id]':45,\
        'question[question_keywords_attributes][0][name]':questionContent,\
        'commit':'Sending','question[prior]':0}
askWhatsay=session.post('https://hinative.com/en-US/questions',params=params)

# 6.From the response, find the question ID for later reuse
bsobj = BeautifulSoup(askWhatsay.text,"html.parser")
questionID = bsobj.find("div",{"class":"box_content"})['ng_init']
print('Your question id is:%s'%questionID)
