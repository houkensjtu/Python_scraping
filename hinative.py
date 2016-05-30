from urllib2 import urlopen
from urllib2 import URLError
from bs4 import BeautifulSoup
from time import sleep
import requests
#proxies = {'http':'http://ch40203515%40shi-g.com:2N%21n9Ly%24\
#          @tnsproxy.shi.co.jp:8080','https':'http://ch4020351\
#          5%40shi-g.com:2N%21n9Ly%24@tnsproxy.shi.co.jp:8080'}

def getHtml(url):
    try:
        html = urlopen(url)
    # In order to handle HTTP error.   
    except URLError as e:
        print(e)
    else:
        return html

def getTitle(html):
    bsobj = BeautifulSoup(html.read(),"html.parser")
#    bsobj = BeautifulSoup(html.text,"html.parser")
    token = bsobj.find("meta",{"name":"csrf-token"})['content']
    return token




html = getHtml('https://hinative.com/en-US/users/sign_in')
token = getTitle(html)
print("Your temporate token is:"+token)

s = requests.Session()
r = s.get('https://hinative.com/en-US/users/sign_in')

bsobj = BeautifulSoup(r.text,"html.parser")
#    bsobj = BeautifulSoup(html.text,"html.parser")
token = bsobj.find("meta",{"name":"csrf-token"})['content']
username = raw_input('Your username: ')
password = raw_input('Your password: ')
params={'user[login]':username,'user[password]':password\
        ,'authenticity_token':token,'user[remember_me]':0,\
        'user[remember_me]':1,'commit':'Sign in'}
r = s.post('https://hinative.com/en-US/users/sign_in',params=params)

#print r.text
#print r.status_code

r = s.get('https://hinative.com/en-US/setting')
#print r.text
#print r.status_code

bsobj = BeautifulSoup(r.text,"html.parser")
userID = bsobj.find("div",{"class":"container js-wrapper"})['data-user-id']
print("Your userID at \"HiNative.com\" is:"+userID)
