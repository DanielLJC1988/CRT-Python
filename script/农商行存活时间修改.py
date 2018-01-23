#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/NSHsite.txt")
writelog = open("c:/Python27/NSHLog.txt","a+")
while True:
	linesite = fping.readline()
	#linelog = writelog.write()
	if linesite:
		crt.Screen.Send(chr(13))
		crt.Screen.WaitForString("#")
		pingIP = str(linesite).strip('\n')
		time.sleep(2)
		crt.Screen.Send("ping  " + linesite  + chr(13))
		time.sleep(3.7)
		crt.Screen.Send( chr(3) )
		time.sleep(0.5)
		ScreenRowPing = crt.Screen.CurrentRow - 2
		outPing = crt.Screen.Get(ScreenRowPing,24,ScreenRowPing,33)
		if (outPing.startswith("2 received") or outPing.startswith("3 received") or outPing.startswith("4 received")):
			crt.Screen.Send("telnet  " + pingIP  + " 2323" + chr(13) )
			crt.Screen.WaitForString("Login: ")
			crt.Screen.Send("admin" + chr(13))
			crt.Screen.WaitForString("Password: ")
			crt.Screen.Send("F@3h|n" + chr(13))
			crt.Screen.WaitForStrings(">")
			crt.Screen.Send("/ip hotspot set 0 idle-timeout=2h keepalive-timeout=1h" + chr(13))
			time.sleep(2)
			crt.Screen.Send("/ip hotspot user profile set [ find default=yes ] shared-users=2 session-timeout=12h idle-timeout=2h keepalive-timeout=1h add-mac-cookie=no" + chr(13))
			time.sleep(2)
			writelog.write(pingIP + "  OK" + "\n")
			
			crt.Screen.Send("/quit" + chr(13))
			time.sleep(1)
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")