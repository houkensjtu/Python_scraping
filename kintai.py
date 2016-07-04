import requests
# Enter your code below:
code = raw_input('Input your employee code:')
password = raw_input('Input your Kintai password:')
params={'syainCode':code, 'RidIndex':'1', 'password':password,'kaisyaCode':'001'}
s = requests.Session()
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/loginSyoki.jsp',params = params)

print(r.text.encode('utf-8'))

# Set your code below, and select month/year.
params = {'syoriSyainCode':'','nyuryokuSyokaiKubun':'002','kosuScreenFlg':'','setteiNen':'2016','setteiGetu':'04'}
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/syokai/tukiSyokai.jsp',params)

print(r.text.encode('utf-8'))
