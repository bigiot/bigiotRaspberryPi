
# -*- coding: utf-8 -*-

import socket
import json
import time
from datetime import datetime
import chitchat as cc

#定义地址及端口
host = '121.42.180.30'
port = 8181

#设备ID及key
DEVICEID='xxx'
APIKEY='xxxxxxx'

data = b''
flag = True

checkin = {"M":"checkin","ID":DEVICEID, "K":APIKEY}
json_checkin = json.dumps(checkin)
#json_checkin = bytes(checkin + '\n', encoding='utf-8')
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
while True:
	try:
		s.connect((host,port))
		break
	except:
		print('连接失败，尝试重新连接!')
		time.sleep(2)

s.send(json_checkin.encode('utf-8'))
s.send(b'\n')
print(json_checkin)
print('\n')
t = time.time()
s.settimeout(0)

def keepOnline(t):
	if time.time()-t>40:
		s.sendall(b'{\"M\":\"status\"}\n')
		print('check status')
		return time.time()
	else:
		return t
	
def say(s, id, coutent):
	saydata = {"M":"say", "ID":id, "C":coutent }
	json_say = json.dumps(saydata)
	s.send(json_say.encode('utf-8'))
	s.send(b'\n')
def process(msg, s, json_checkin):
	json_data = json.loads(msg)
	print(json_data)
	if json_data['M'] == 'say':
		print("接收到的数据：", json_data)
		print("平台指令：",json_data['C'])
		#test.chitchat(json_data['C'])
		say(s, json_data['ID'], cc.chitchat(json_data['C']))
	if json_data['M'] == 'connected':
		s.send(json_checkin.encode('utf-8'))
		s.send(b'\n')
	if json_data['M'] == 'login':
		say(s, json_data['ID'], '你好！我是小冰，请问有什么可以帮你！')
		#say(s, json_data['ID'], 'Welcome! Your public ID is '+json_data['ID'])
		
while True:
	try:
		d=s.recv(1)
		flag=True
	except:
		flag=False
		time.sleep(2)
		t = keepOnline(t)
		
	if flag:
		if d!=b'\n':
			data+=d
		else:
			#do something here...
			msg=str(data,encoding='utf-8')
			process(msg,s,json_checkin)
			data=b''

	
