import socket

HOST = '172.27.112.40'
PORT = 80
data = "POST /servlet/RTRRDisplayConfig HTTP/1.1\r\nHost: 172.27.112.40\r\nAccept-Encoding: identity\r\nCookie: JSESSIONID=487D7BDC9E91CC65603A7FB5A16B7E11\r\n\r\n"
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" , "Cookie": "JSESSIONID=487D7BDC9E91CC65603A7FB5A16B7E11" }
print data
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST , PORT))
s.sendall(data)

data = s.recv(8192)
s.close()
print data
