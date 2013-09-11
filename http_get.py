import socket

HOST = '127.0.0.1'
PORT = 8080
data = '''
GET / HTTP/1.0\r\n
\r\n
'''
print data
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((HOST , PORT))
s.sendall(data)
data = s.recv(2048)
s.close()
print data
