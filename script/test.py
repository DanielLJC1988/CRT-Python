#! python2
import re
import sys
import os
import pyotp

def password():
	T = pyotp.TOTP('AXX6DUCLASSE3DP7')
	PWD = 'lujc' + T.now()

	#f1 = open("c:/a.txt",'w')
	#f1.write(PWD)
	#f1.close()
	#print PWD
	return PWD
PSW = password()
print (PSW)

