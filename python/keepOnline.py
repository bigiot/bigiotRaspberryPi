#!/usr/bin/python3
import socket
import time
from datetime import datetime
#must be modified===
DEVICEID='112'
#modify end=========
host="www.bigiot.net"
port=8181
checkinBytes=bytes('{\"M\":\"checkin\",\"ID\":\"'+DEVICEID+'\",\"K\":\"'+APIKEY+'\"}\n',encoding='utf8')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.settimeout(0)
s.sendall(checkinBytes)
data=b''
flag=1
t=time.time()
def keeponline(t):
	if time.time()-t>30:
		s.sendall(b'{\"M\":\"status\"}\n')
		print('check status')
		return time.time()
	else:
		return t
while True:
	try:
		d=s.recv(1)
		flag=True
	except:
		flag=False
	if flag:
		if d!=b'\n':
			data+=d
		else:
			#do something here...
			print(str(data,encoding='utf-8'))
			data=b''
	t = keeponline(t)
