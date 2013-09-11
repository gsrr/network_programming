import httplib
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" , "Cookie": "JSESSIONID=487D7BDC9E91CC65603A7FB5A16B7E11" }
conn = httplib.HTTPConnection("172.27.112.40")
conn.request("POST", "/servlet/RTRRDisplayConfig" , "" , headers)
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
conn.close()