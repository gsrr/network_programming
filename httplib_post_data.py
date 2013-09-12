import httplib
import urllib
params = urllib.urlencode({'RTRR_name': 'RTRR_20130905_1700'})
headers = {"Cookie": "JSESSIONID=59AFF0FF0BEBA159EFAD6C4108BE7488" , "Content-Length":"28" , "Content-Type":"application/x-www-form-urlencoded"}
conn = httplib.HTTPConnection("172.27.112.40")
conn.request("POST", "/servlet/GetConfigData" , params, headers)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1 

conn.close()