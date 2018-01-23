#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/PPJsite.txt")
writelog = open("c:/Python27/PPJLog.txt","a+")
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
			crt.Screen.Send("telnet  " + pingIP  + chr(13) )
			crt.Screen.WaitForString("Username: ")
			crt.Screen.Send("fashion" + chr(13))
			crt.Screen.WaitForString("Password: ")
			crt.Screen.Send("fashion-tele" + chr(13))
			crt.Screen.WaitForStrings("#")
			crt.Screen.Send("show ip inter brief" + chr(13))
			time.sleep(2)
			screenrow = crt.Screen.CurrentRow - 2
			out = crt.Screen.Get(screenrow,28,screenrow,43)
			rfind = out.rfind('.254')
			crt.Screen.Send("conf t" + chr(13))
			time.sleep(0.5)
			crt.Screen.Send("ip access-list extended vlan1" + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("11 deny ip host " + out[:rfind] + ".135 any" + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("12 deny ip host " + out[:rfind] + ".136 any" + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("ip access-list extended vlan2_nat" + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("11 permit ip host " + out[:rfind] + ".135 any" + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("12 permit ip host " + out[:rfind] + ".136 any" + chr(13))
			time.sleep(0.3)
			writelog.write(pingIP + "  OK" + "\n")
			
			crt.Screen.Send("end" + chr(13) + "wr" + chr(13))
			time.sleep(8)
			crt.Screen.Send("exit" + chr(13))
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")