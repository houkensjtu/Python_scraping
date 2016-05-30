import requests
# Enter your code below:
params={'syainCode':'', 'RidIndex':'1', 'password':'','kaisyaCode':'001'}
s = requests.Session()
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/loginSyoki.jsp',params = params)

# print r.text

# Set your code below, and select month/year.
params = {'syoriSyainCode':'','nyuryokuSyokaiKubun':'002','kosuScreenFlg':'','setteiNen':'','setteiGetu':''}
r = s.post('http://jforpe.shi.co.jp/time/timeSheet/syokai/tukiSyokai.jsp',params)

print r.text
