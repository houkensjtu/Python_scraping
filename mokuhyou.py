import requests

# Set your code and password below:
params={'syainCode':'', 'password':'', 'kaisyaCode':'0001'}
s = requests.Session()
r = s.post('http://j-forpeap.shi.co.jp/mboHome/mbo/loginSyoki.jsp',params = params)

print r.text

r = s.get('http://j-forpeap.shi.co.jp/mboHome/mbo/frame.jsp')

print r.text
