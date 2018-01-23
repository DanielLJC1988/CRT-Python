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
		time.sleep(8)
		#crt.Screen.Send( chr(17) + chr(16) + chr(54)  )
		time.sleep(0.3)
		ScreenRowPing = crt.Screen.CurrentRow - 2
		outPing = crt.Screen.Get(ScreenRowPing,1,ScreenRowPing,5)
		if (outPing.startswith("!!!!!") or outPing.startswith(".!!!!") or outPing.startswith("!.!!!")):
			crt.Screen.Send("telnet  " + pingIP + chr(13) )
			crt.Screen.WaitForString("Username: ")
			crt.Screen.Send("fashion" + chr(13))
			crt.Screen.WaitForString("Password: ")
			crt.Screen.Send("fashion-tele" + chr(13))
			crt.Screen.WaitForStrings(">")
			crt.Screen.Send("en" + chr(13))
			crt.Screen.WaitForString("Password: ")
			crt.Screen.Send("1^pvbM^a" + chr(13))
			crt.Screen.WaitForStrings("#")
			crt.Screen.Send("show runn | se ip route " + chr(13))
			time.sleep(2)
			screenrow = crt.Screen.CurrentRow - 3
			out = crt.Screen.Get(screenrow,26,screenrow,60)
			######rfind = out.rfind('.254')
			crt.Screen.Send("conf t" + chr(13))
			time.sleep(0.5)
			##crt.Screen.Send("ip route 192.168.255.0 255.255.255.0 169.3.24.1 name fashion-TYMGM   " + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("ip route 58.246.64.26 255.255.255.255 "  + out + " name adidas-cu   " + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("ip route 61.151.249.2 255.255.255.255 "  + out + " name fashion-mgm " + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("ip route 222.73.198.0 255.255.255.0   "  + out + " name fashion-mgm " + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("ip route 180.169.58.70 255.255.255.255 " + out + " name adidas-ct  "  + chr(13))
			time.sleep(0.3)
			crt.Screen.Send("no ip route 0.0.0.0 0.0.0.0 " + out  + chr(13))
			time.sleep(0.3)
			
			
			writelog.write(pingIP + "  OK" + "\n")
			crt.Screen.Send("end" + chr(13))
			crt.Screen.Send("wr" + chr(13))
			time.sleep(4)
			crt.Screen.Send("exit" + chr(13))
			time.sleep(2)
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")