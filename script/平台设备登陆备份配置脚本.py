#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

def Copyconfig():
	crt.Screen.IgnoreCase = True

	fping = open(r"c:/Python27/allsite.txt")
	writelog = open("c:/Python27/allLog.txt","a+")

	while True:
		time.sleep(0.3)
		linesite = fping.readline()
		if linesite:
			crt.Screen.Send(chr(13))
			crt.Screen.WaitForString("#")
			pingIP = str(linesite).strip('\n')
			crt.Screen.Send("ping  " + pingIP  + chr(13))
			time.sleep(3.7)
			crt.Screen.Send( chr(3) )
			time.sleep(0.3)
			ScreenRowPing = crt.Screen.CurrentRow - 2
			outPing = crt.Screen.Get(ScreenRowPing,24,ScreenRowPing,33)
			if (outPing in ["2 received", "3 received", "4 received"]):
				crt.Screen.Send("telnet " + pingIP  + chr(13) )
				time.sleep(2)
				crt.Screen.WaitForString("Username:",2)
				crt.Screen.Send("lujc" + chr(13))
				time.sleep(0.2)
				crt.Screen.WaitForString("Password:",2)
				code = os.popen('python c:/Python27/test.py').read()
				time.sleep(0.2)
				crt.Screen.Send(code)
				time.sleep(3)

				crt.Screen.Send(chr(13) )
				crt.Screen.WaitForStrings("#",2)
				ScreenRowHostname = crt.Screen.CurrentRow
				outHostname = crt.Screen.Get(ScreenRowHostname,1,ScreenRowHostname,35)
				outHostname = str(outHostname).strip(' ')
				crt.Dialog.MessageBox(outHostname)
				#开始拷贝配置--------------------------------------------------------------------------------------------------------
				writelog.write( outHostname + "\n")
				crt.Screen.Send("show runn" + chr(13))
				time.sleep(3)
				while True:
					crt.Screen.Send(chr(13))
					if (crt.Screen.WaitForString("#",2) == False):
						time.sleep(1)
						ScreenRowShow = crt.Screen.CurrentRow
						printScreen = crt.Screen.Get2(1,1,31,150);
						#crt.Dialog.MessageBox( printScreen)
						writelog.write(printScreen )
						time.sleep(0.1)
						crt.Screen.Send(" ")
					else:
						#保存最后一次屏幕数据
						printScreenFinnal = crt.Screen.Get2(1,1,31,150);
						writelog.write(printScreenFinnal + "\n")
						writelog.write( outHostname + " Config copy completed" + "\n\n\n\n\n")
						break
				#--------------------------------------------------------------------------------------------------------------------------			
				time.sleep(2)
				crt.Screen.Send("exit" + chr(13) )
				time.sleep(1)
				crt.Screen.Clear()
				time.sleep(2)
				
			else:
				writelog.write(pingIP + "  telnet time out " + "\n")
				time.sleep(3)
				continue
			
		else:
			break
	fping.close()
	writelog.close()
	crt.Dialog.MessageBox("Script completed")
	
Copyconfig()