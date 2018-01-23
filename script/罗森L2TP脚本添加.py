#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/luosensite.txt")
writelog = open("c:/Python27/luosenLog.txt","a+")
while True:
	linesite = fping.readline()
	#linelog = writelog.write()
	if linesite:
		crt.Screen.Send(chr(13))
		crt.Screen.WaitForString("#")
		pingIP = str(linesite).strip('\n')
		crt.Screen.Send("ping  " + linesite  + chr(13))
		time.sleep(3.7)
		crt.Screen.Send( chr(3) )
		time.sleep(0.3)
		ScreenRowPing = crt.Screen.CurrentRow - 2
		outPing = crt.Screen.Get(ScreenRowPing,24,ScreenRowPing,33)
		if (outPing.startswith("2 received") or outPing.startswith("3 received") or outPing.startswith("4 received")):
			crt.Screen.Send("telnet  " + pingIP + " 2323" + chr(13) )
			crt.Screen.WaitForString("Login: ")
			crt.Screen.Send("admin" + chr(13))
			crt.Screen.WaitForString("Password: ")
			crt.Screen.Send("F@3h|n" + chr(13))
			crt.Screen.WaitForStrings(">")
			f1 = open(r"c:/Python27/luosenL2TP.txt")
			while True:
				line = f1.readline()
				if line:
					crt.Screen.Send(line)
					crt.Screen.Send(chr(13))
					time.sleep(0.2)
				else:
					break
			writelog.write(pingIP + "  OK" + "\n")
			
			f1.close()
			crt.Screen.Send("/" + chr(13) + "quit" + chr(13))
			crt.Screen.Send("quit" + chr(13))
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")