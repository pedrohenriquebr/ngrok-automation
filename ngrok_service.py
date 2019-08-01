import json
import os
import sys
import settings
from smtpclient import SMTPClient
import time
import subprocess

class NgrokService:
	def __init__(self, email,password):
		self.email = email
		self.password = password
		self.client  = SMTPClient('smtp.gmail.com',email,password)

	def start(self,cmd,send_email=False):
		os.system("killall ngrok")

		subprocess.Popen(
			['/usr/bin/env','bash','-c','ngrok {} -config /home/pedro/.ngrok2/ngrok.yml'.format(cmd)],
			stdout=open('ngrok.log','w'),
			stderr=open('ngrok.err','w'))
		
		time.sleep(10)
		
		os.system("curl -s http://localhost:4040/api/tunnels > tunnels.json")
		
		with open('tunnels.json') as data_file:
			datajson = json.load(data_file)
			
		msg = "ngrok URL's: \n"
		for i in datajson['tunnels']:
			msg = msg + i['public_url'] +'\n'
		
		if send_email:
			self.client.sendMail("Ngrok service",[self.email],msg)
		
		return msg

	def stop(self):
		os.system("killall ngrok")
		
if __name__ == "__main__":

	email = os.getenv("SMTPCLIENT_EMAIL")
	password = os.getenv("SMTPCLIENT_PASSWORD")

	if email is None or password is None:
		print("You have to declare SMTPCLIENT_EMAIL and SMTPCLIENT_PASSWORD!")
		exit(1)
	
	if len(sys.argv) != 3 :
		print('{} <protocol> <port>'.format(sys.argv[0]))
		print('Examples:\n{} http 1234\n{} tcp 1234\n'.format(sys.argv[0],sys.argv[0]))
		exit(1)
	
	ngs = NgrokService(email,password)
	print(ngs.start(' '.join(sys.argv[1:]),send_email=True))