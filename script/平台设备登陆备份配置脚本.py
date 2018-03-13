#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time
import datetime

def Main():
	crt.Screen.IgnoreCase = True

	fping = open(r"c:/Python27/allsite.txt")
	writelog = open("c:/Python27/allLog.txt","a+")
	now = datetime.datetime.now()
	timeNow = now.strftime('%Y.%m.%d')
	path=r'c:/PythonLog/' + timeNow
	#os.makedirs(path)
	if os.path.exists('c:/PythonLog/' + timeNow) == False:
		os.mkdir(path)

	while True:
		time.sleep(0.3)
		line = fping.readline()
		if line:
			#读取txt文件一行数据，并根据下标,截取内网IP的字符并替换掉\t符号
			linesite = str(line).split(',')[0].strip('\t')
			#读取设备类型
			machine_type = str(line).split(',')[1].strip('\t\n')
			
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
				crt.Screen.Send("ssh -l lujc " + pingIP  + chr(13) )
				if (crt.Screen.WaitForString("?",4)):
					crt.Screen.Send("yes" + chr(13))
				
				#crt.Screen.WaitForStrings("Username:",2)
				#crt.Screen.Send("lujc" + chr(13))
				#time.sleep(0.2)
				crt.Screen.WaitForStrings("assword:",6)
				code = os.popen('python c:/Python27/test.py').read()
				time.sleep(0.2)
				crt.Screen.Send(code)
				#time.sleep(2)
				
				#加入判断还需要enable密码的设备----------------
				if (machine_type == 'cisco' and crt.Screen.WaitForStrings(">",5)):
					crt.Screen.Send("en" + chr(13))
					time.sleep(0.2)
					crt.Screen.Send("fashion-tele" + chr(13))
					crt.Screen.Send(chr(13))
					crt.Screen.WaitForStrings("#",2)
				#-----------------------------------------------			
				'''
				#-----------当OTP中断时，本地账号登陆-----------
				if (crt.Screen.WaitForStrings("Username:",30)):
					crt.Screen.Send("fashion" + chr(13))
					crt.Screen.WaitForStrings("Password:",3)
					crt.Screen.Send("F@shion_Mgm@403" + chr(13))
					if machine_type == 'cisco':
						if (crt.Screen.WaitForStrings(">",20)):
							crt.Screen.Send("en" + chr(13))
							time.sleep(0.2)
							crt.Screen.Send("cisco" + chr(13))
							crt.Screen.Send(chr(13) )
							crt.Screen.WaitForStrings("#",2)
						else:
							crt.Screen.Send(chr(13) )
							crt.Screen.WaitForStrings("#",2)
					else:
						crt.Screen.Send(chr(13))
				#-----------------------------------------------
				'''
				time.sleep(5)
				ScreenRowHostname = crt.Screen.CurrentRow
				outHostname = crt.Screen.Get(ScreenRowHostname,1,ScreenRowHostname,35)
				outHostname = str(outHostname).strip(' <> ')
				#crt.Dialog.MessageBox(outHostname)
				#开始拷贝配置--------------------------------------------------------------------------------------------------------
				writelog.write( outHostname + "\n")
				writeCreate = open(r"c:/PythonLog/" + timeNow + "/" + outHostname + ".txt","a")
				#判断是cisco设备还是华为设备
				if machine_type == 'cisco':
					crt.Screen.Send("show runn" + chr(13))
					time.sleep(3)
					while True:
						#crt.Screen.Send(chr(13))
						if (crt.Screen.WaitForStrings(outHostname,2) == False):
							time.sleep(0.3)
							ScreenRowShow = crt.Screen.CurrentRow
							printScreen = crt.Screen.Get2(1,1,29,150);
							#crt.Dialog.MessageBox( printScreen)
							writeCreate.write(printScreen )
							time.sleep(0.1)
							crt.Screen.Send(" ")
						else:
							#保存最后一次屏幕数据
							printScreenFinnal = crt.Screen.Get2(1,1,29,150);
							writeCreate.write(printScreenFinnal + "\n")
							writeCreate.write( outHostname + " Config copy completed" + "\n\n\n\n\n")
							break
					time.sleep(2)
					crt.Screen.Send("exit" + chr(13) )
					time.sleep(1)
					#清空屏幕
					crt.Screen.Clear()
					writeCreate.close()
					time.sleep(2)
				
				elif machine_type == 'HW':
					crt.Screen.Send("display current-configuration " + chr(13))
					time.sleep(3)
					while True:
						#crt.Screen.Send(chr(13))
						outHostnameHW = '<' + outHostname + '>'
						if (crt.Screen.WaitForStrings(outHostnameHW,2) == False):
							time.sleep(0.3)
							ScreenRowShow = crt.Screen.CurrentRow
							printScreen = crt.Screen.Get2(1,1,29,150);
							#crt.Dialog.MessageBox( printScreen)
							writeCreate.write(printScreen )
							time.sleep(0.1)
							crt.Screen.Send(" ")
						else:
							#保存最后一次屏幕数据
							printScreenFinnal = crt.Screen.Get2(1,1,29,150);
							writeCreate.write(printScreenFinnal + "\n")
							writeCreate.write( outHostnameHW + " Config copy completed" + "\n\n\n\n\n")
							break
					time.sleep(2)
					crt.Screen.Send("quit" + chr(13) )
					time.sleep(1)
					#清空屏幕
					crt.Screen.Clear()
					writeCreate.close()
					time.sleep(2)
						
				#--------------------------------------------------------------------------------------------------------------------------			
				##alt+p键组合------alt对应chr(18),ctrl对应chr(17)
				##crt.Screen.Send(chr(18) + chr(112))
				##crt.Dialog.MessageBox('test')
				
			else:
				writelog.write(pingIP + "  telnet time out " + "\n")
				time.sleep(3)
				continue
			
		else:
			break
	fping.close()
	writelog.close()
	crt.Dialog.MessageBox("Script completed")
	
Main()