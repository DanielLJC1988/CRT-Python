#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/allsite.txt")
writelog = open("c:/Python27/allLog.txt","a+")
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
			crt.Screen.Send("ssh -l ideal " + pingIP  + chr(13) )
			if (crt.Screen.WaitForString("?",4)):#crt.Screen.WaitForString("?")
				crt.Screen.Send("yes" + chr(13))
				
				
			crt.Screen.WaitForString("Password: ",3)
			time.sleep(0.5)
			crt.Screen.Send("888888" + chr(13))
			crt.Screen.WaitForStrings("#")
			crt.Screen.Send("show ip inter brief | include Tunnel102" + chr(13))
			time.sleep(3)
			ScreenRowTunnel = crt.Screen.CurrentRow - 1
			outTunnel102 = crt.Screen.Get(ScreenRowTunnel,0,ScreenRowTunnel,80)
			writelog.write(pingIP + "  " + outTunnel102 + "\n")
			
			
			crt.Screen.Send(chr(13) + "exit" + chr(13) )
			time.sleep(1)
			#crt.Screen.Send("quit" + chr(13))
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			time.sleep(1)
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")