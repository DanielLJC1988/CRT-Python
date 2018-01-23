#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time


crt.Screen.IgnoreCase = True
crt.Screen.WaitForString("Username")
crt.Screen.Send("fashion\r\n")
crt.Screen.WaitForString("Password")
crt.Screen.Send("fashion@123\r\n")
crt.Screen.WaitForString("VPNServer")
crt.Screen.Send("en\r\n")
crt.Screen.WaitForString("Password")
crt.Screen.Send("fashion@123\r\n")
crt.Screen.WaitForString("#")
f1 = open(r"c:/Python27/a.txt")
while True:
	line = f1.readline()
	if line:
		password = str(line).strip('\n')
		#password = crt.Dialog.Prompt("IP address","tittle","",False) 
		crt.Screen.Send("ping "+ password + " re 10\n")
		outPut = crt.Screen.ReadString(["!!!!!!!!!!","!!!!!!!"],20)
		time.sleep(0.2)
		index = crt.Screen.MatchIndex
		if (index == 0):
			crt.Dialog.MessageBox("Time out!")
		elif (index == 1):
			crt.Dialog.MessageBox("Ping OK")
		elif (index == 2):
			crt.Dialog.MessageBox("Ping Nice")
	else:
		break
f1.close()


