from urllib2 import urlopen, Request
from urllib import urlencode

# Set your code and password below:
params={'syainCode':'', 'password':'','kaisyaCode':'0001'}
encodeddata = urlencode(params)

r1 = urlopen('http://j-forpeap.shi.co.jp/mboHome/mbo/loginSyoki.jsp',encodeddata)
cookie = r1.headers.get('Set-Cookie')
print r1.read()
print cookie


r2 = Request('http://j-forpeap.shi.co.jp/mboHome/mbo/frame.jsp')
r2.add_header('cookie', cookie)
response = urlopen(r2)

cookie = response.headers.get('Set-Cookie')

print response.read()
print cookie
