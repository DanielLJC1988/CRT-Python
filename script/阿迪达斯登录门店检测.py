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
crt.Screen.WaitForStrings("VPNServer")
crt.Screen.Send("en\r\n")
crt.Screen.WaitForString("Password")
crt.Screen.Send("fashion@123\r\n")
crt.Screen.WaitForString("#")
crt.Screen.Send("show ip nhrp brief\r\n")
#while crt.Screen.WaitForString("--More--"):
	#crt.Screen.Send(" ")
	#if crt.Screen.WaitForString("#"):
		#break
time.sleep(1)
crt.Screen.WaitForString("#")

siteip = crt.Dialog.Prompt("输入需要检测的门店IP地址：","门店IP","",False)
crt.Screen.Send("telnet "+ siteip + "\r\n" )
crt.Screen.WaitForString("Username")
crt.Screen.Send("fashion\r\n")
crt.Screen.WaitForString("Password")
crt.Screen.Send("fashion-tele\r\n")
crt.Screen.WaitForStrings(">")
crt.Screen.Send("en\r\n")
crt.Screen.WaitForString("Password")
crt.Screen.Send("1^pvbM^a\r\n")

f1 = open(r"c:/Python27/a.txt")
while True:
	line = f1.readline()
	if line:
		password = str(line).strip('\n')
		#password = crt.Dialog.Prompt("IP address","tittle","",False) 
		crt.Screen.Send("ping "+ password + " source vlan1 re 10\n")
		outPut = crt.Screen.ReadString(["!!!!!!!!!!","!!!!!!!"],20)
		time.sleep(0.2)
		index = crt.Screen.MatchIndex
		if (index == 0):
			crt.Dialog.MessageBox("超时无法到达总部内网IP，请转NOC查看！！！")
		elif (index == 1):
			crt.Dialog.MessageBox("检测到阿迪总部内网IP地址正常")
		elif (index == 2):
			crt.Dialog.MessageBox("检测到阿迪总部内网IP地址无丢包")
		else:
			crt.Dialog.MessageBox("到总部有丢包，请转NOC查看！！")
	else:
		break
f1.close()


