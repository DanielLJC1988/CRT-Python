#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/MDCsite.txt")
writelog = open("c:/Python27/MDClog.txt","a+")
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
		if (outPing.startswith("1 received") or outPing.startswith("2 received") or outPing.startswith("3 received") or outPing.startswith("4 received")):
			crt.Screen.Send("ssh -l ideal  " + pingIP  + chr(13) )
			time.sleep(2)
			ScreenRowPing3 = crt.Screen.CurrentRow - 1
			outPing3 = crt.Screen.Get(ScreenRowPing,36,ScreenRowPing,62)
			if (outPing3.startswith("port 22: Connection refused")):
				writelog.write(pingIP + " ssh port 22: Connection refused")
				continue
				
			else:
				#crt.Screen.WaitForString("(yes/no)? ")
				#time.sleep(3)
				#crt.Screen.Send("yes" + chr(13))
				crt.Screen.WaitForString("Password: ")
				crt.Screen.Send("888888" + chr(13))
				crt.Screen.WaitForStrings("#")
				crt.Screen.Send("ping 10.125.32.1" + chr(13))
				time.sleep(12)
				ScreenRowPing2 = crt.Screen.CurrentRow - 2
				outPing2 = crt.Screen.Get(ScreenRowPing,1,ScreenRowPing,5)
				if (outPing2.startswith("!!!!!") or outPing2.startswith(".!!!!") or outPing2.startswith("..!!!") or outPing2.startswith(".!!.!") or outPing2.startswith(".!!!.") or outPing2.startswith("!!!!.")):
					crt.Screen.Send("conf t" + chr(13))
					time.sleep(0.5)
					crt.Screen.Send("router eigrp 23" + chr(13))
					time.sleep(0.3)
					crt.Screen.Send("no offset-list OFF_BLINK_OUT out 5000000 Tunnel100 " + chr(13))
					time.sleep(0.3)
					crt.Screen.Send("no offset-list OFF_BLINK_IN in 5000000 Tunnel100 " + chr(13))
					time.sleep(0.3)
					crt.Screen.Send("offset-list OFF_BLINK_OUT out 5000000 Tunnel101 " + chr(13))
					time.sleep(0.3)
					crt.Screen.Send("offset-list OFF_BLINK_IN in 5000000 Tunnel101 " + chr(13))
					time.sleep(0.3)
					writelog.write(pingIP + "  OK" + "\n")
					crt.Screen.Send("end" + chr(13) + "wr" + chr(13))
					time.sleep(6)
					crt.Screen.Send("exit" + chr(13))
					time.sleep(2)
					continue
				else:
					writelog.write(pingIP + " tunnel 100 is down!!  so not change tunnel!" + "\n")
					crt.Screen.Send("exit" + chr(13))
					time.sleep(2)
					continue
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")