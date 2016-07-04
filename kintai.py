import requests
from bs4 import BeautifulSoup

# Enter your code below:
code = raw_input('Input your employee code:')
password = raw_input('Input your Kintai password:')
params={'syainCode':code, 'RidIndex':'1', 'password':password,'kaisyaCode':'001'}

# Create the working session:
s = requests.Session()
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/loginSyoki.jsp',params = params)

# print(r.text.encode('utf-8'))

# Set your code below, and select month/year.
params = {'syoriSyainCode':'','nyuryokuSyokaiKubun':'002','kosuScreenFlg':'','setteiNen':'2016','setteiGetu':'04'}
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/syokai/tukiSyokai.jsp',params)
bsobj = BeautifulSoup(r.text.encode('utf-8'),"html.parser")

# From returned result, grab the working hour information:
regularWorkhour = bsobj.find_all("table", {"class","daymonth"})[0].find_all("tr")[1].find_all("td")[0]
actualWorkhour = bsobj.find_all("table", {"class","daymonth"})[0].find_all("tr")[1].find_all("td")[1]
# print(r.text.encode('utf-8'))

print("Your regular working hour in 2016.4:")
print(regularWorkhour)
print("Your actual working hour in 2016.4:")
print(actualWorkhour)

