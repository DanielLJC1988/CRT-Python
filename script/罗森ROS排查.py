#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True

crt.Screen.WaitForString("#")
siteip = crt.Dialog.Prompt("Enter site IP","site IP","",False)
crt.Screen.Send("telnet %s 2323\r\n" %siteip)
crt.Sleep(1000)
crt.Screen.WaitForString("Login: ")
crt.Screen.Send("admin" + chr(13))
crt.Screen.WaitForString("Password: ")
crt.Screen.Send("fashion" + chr(13))
crt.Screen.WaitForStrings(">")
crt.Screen.Send("ip add print\r\n")
crt.Screen.WaitForString(">")
screenrow = crt.Screen.CurrentRow - 3
out = crt.Screen.Get(screenrow,6,screenrow,40)
rfind = out.rfind("/")
#out[:rfind]
f1 = open(r"c:/Python27/luosen.txt")
while True:
	line = f1.readline()
	if line:
		password = str(line).strip('\n')
		crt.Screen.Send("ping " + password + " src-address=" + out[:rfind] + " count=5 \r\n")
		#crt.Sleep(3000)
		#crt.Screen.Send(chr(3))						#ctrl-c»°œ˚ping£¨∑¿÷πtime out ±ø®À¿
		
		#outPut = crt.Screen.ReadString(["packet-loss=0\%","packet-loss=100\%"],10)
		time.sleep(6)
		ScreenRowPing = crt.Screen.CurrentRow - 2
		outPing = crt.Screen.Get(ScreenRowPing,12,ScreenRowPing,22)
		rfindPing = outPing.rfind(" ")
		if (outPing[:rfindPing].startswith("received=5")):
			crt.Dialog.MessageBox("Ping OK! packet-loss=0%")
		elif (outPing[:rfindPing].startswith("received=0")):
			crt.Dialog.MessageBox("Time out! packet-loss=100%")
		else:
			crt.Dialog.MessageBox("Ping OK, has packet loss!")
	else:
		break
f1.close()