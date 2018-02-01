#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

#开启CRT屏幕显示同步
crt.Screen.IgnoreCase = True

#存放需要加备份门店内网IP及Tunnel102接口IP的表格路径
fping = open(r"c:/Python27/allsite.txt")
#存放日志文件的路径
writelog = open("c:/Python27/allLog.txt","a+")
while True:
	time.sleep(0.3)
	linesite = fping.readline()
	#linelog = writelog.write()
	if linesite:
		crt.Screen.Send(chr(13))
		crt.Screen.WaitForString("#")
		
		#读取txt文件一行数据，并根据下标,截取内网IP的字符并替换掉\t符号
		pingIP = str(linesite).split(',')[0].strip('\t')
		#读取txt文件一行数据，并根据下标,截取tunnel IP的字符并替换掉\t\n符号
		tunnel102IP = str(linesite).split(',')[1].strip('\t\n')
		
		#输出ping测内网IP,是否能通
		crt.Screen.Send("ping  " + pingIP  + chr(13))
		time.sleep(3.7)
		crt.Screen.Send( chr(3) )
		time.sleep(0.3)
		ScreenRowPing = crt.Screen.CurrentRow - 2
		outPing = crt.Screen.Get(ScreenRowPing,24,ScreenRowPing,33)
		if (outPing.startswith("2 received") or outPing.startswith("3 received") or outPing.startswith("4 received")):
			crt.Screen.Send("ssh -l ideal " + pingIP  + chr(13) )
			if (crt.Screen.WaitForString("?",2)):
				crt.Screen.Send("yes" + chr(13))
				
				
			crt.Screen.WaitForString("Password: ",3)
			time.sleep(0.5)
			crt.Screen.Send("888888" + chr(13))
			crt.Screen.WaitForStrings("#")
			
			
			#查看各地址---------------------------------------------------------------------------------------------------------------------			
			#查看eigrp号区分不同POP点门店
			while True:
				crt.Screen.Send("show ip eigrp interfaces " + chr(13))
				time.sleep(6)
				ScreenRowEigrp = crt.Screen.CurrentRow - 5
				#outEigrpNum 获取的eigrp号
				outEigrpNum = crt.Screen.Get(ScreenRowEigrp,30,ScreenRowEigrp,31)
				#crt.Dialog.MessageBox( outEigrpNum)
				if (outEigrpNum == "  " or outEigrpNum == "/0"):
					ScreenRowEigrp1 = crt.Screen.CurrentRow - 3
					outEigrpNum = crt.Screen.Get(ScreenRowEigrp1,30,ScreenRowEigrp1,31)
					crt.Dialog.MessageBox( outEigrpNum)
					time.sleep(3)
					crt.Screen.Send("conf t " + chr(13))
					time.sleep(0.2)
					crt.Screen.Send("no router eigrp " + outEigrpNum + chr(13))
					time.sleep(0.2)
					crt.Screen.Send("end " + chr(13))
					time.sleep(0.2)
					continue
				else:
					#判断是否正确取到eigrp的号，避免影响后面刷配置
					if (outEigrpNum in ["10", "20", "21", "23", "24"]):
						break
					else:
						continue
					
			
			#查看获取tunnel source 接口
			crt.Screen.Send("show runn | se tunnel source " + chr(13))
			time.sleep(4)
			ScreenRowTunnelSource = crt.Screen.CurrentRow - 1
			#outTunnelSource 获取的tunnel source接口
			outTunnelSource = crt.Screen.Get(ScreenRowTunnelSource,16,ScreenRowTunnelSource,35)
			#crt.Dialog.MessageBox( outTunnelSource)
			time.sleep(0.2)
			
			#查看获取下一条网关地址/接口
			while True:
				crt.Screen.Send("show runn | se ip route 116.236.238.173 " + chr(13))
				time.sleep(4)
				ScreenRowGw = crt.Screen.CurrentRow - 1
				#outGw 获取的下一条网关地址/接口
				outGw = crt.Screen.Get(ScreenRowGw,42,ScreenRowGw,70)
				if (outGw == " 116.236.238.173             "):
					crt.Screen.Send("show runn | se ip route 116.246.14.201 " + chr(13))
					time.sleep(4)
					ScreenRowGw1 = crt.Screen.CurrentRow - 1
					outGw = crt.Screen.Get(ScreenRowGw1,41,ScreenRowGw1,70)
					if (outGw == "e 116.246.14.201              "):
						crt.Screen.Send("show runn | se ip route 114.80.232.134 " + chr(13))
						time.sleep(4)
						ScreenRowGw2 = crt.Screen.CurrentRow - 1
						outGw = crt.Screen.Get(ScreenRowGw2,41,ScreenRowGw2,70)
						crt.Dialog.MessageBox("非标的网关注意下")
						crt.Dialog.MessageBox( outGw)
						time.sleep(0.2)
						break
						
					else:
						break
					
				else:
					#crt.Dialog.MessageBox( outGw)
					break
					time.sleep(0.2)
			
			#查看获取内网IP
			crt.Screen.Send("show ip inter brief | include  Vlan10 " + chr(13))
			time.sleep(6)
			ScreenRowLan = crt.Screen.CurrentRow - 1
			#outLan 获取内网IP
			outLan = crt.Screen.Get(ScreenRowLan,28,ScreenRowLan,42)
			time.sleep(0.2)
			outLan0 = outLan.split('.')[0]
			outLan1 = outLan.split('.')[1]
			outLan2 = outLan.split('.')[2]
			#outLanFinal 拼接可用IP网段
			outLanFinal = outLan0 + '.' + outLan1 + '.' + outLan2 + '.' + '0'
			#crt.Dialog.MessageBox( outLanFinal)
			time.sleep(0.2)
			
			
			#查看获取Tunnel100地址
			crt.Screen.Send("show ip inter brief | include Tunnel100 " + chr(13))
			time.sleep(4)
			ScreenRowTunnel100 = crt.Screen.CurrentRow - 1
			#outTunnel100 获取Tunnel100地址
			outTunnel100 = crt.Screen.Get(ScreenRowTunnel100,28,ScreenRowTunnel100,42)
			#crt.Dialog.MessageBox( outTunnel100)
			time.sleep(0.2)
			
			#查看获取Tunnel101地址
			crt.Screen.Send("show ip inter brief | include Tunnel101 " + chr(13))
			time.sleep(4)
			ScreenRowTunnel101 = crt.Screen.CurrentRow - 1
			#outTunnel101 获取Tunnel101地址
			outTunnel101 = crt.Screen.Get(ScreenRowTunnel101,28,ScreenRowTunnel101,42)
			#crt.Dialog.MessageBox( outTunnel101)
			time.sleep(0.2)
			
			
			#--------------------------------------------------------------------------------------------------------------------			
			
				
			#开始配置设备--------------------------------------------------------------------------------------------------------
			crt.Screen.Send("conf t" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no track 1" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no track 2" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no track 3" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no ip sla 1" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no ip sla 2" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no ip sla 3" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("username admin privilege 15 secret 0 admincisco" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip access-list extended ISP_Firewall" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("no deny   ip any any" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("permit ip host 61.151.249.45 any" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("deny   ip any any log" + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip route 61.151.249.45 255.255.255.255 " + outGw  + chr(13))
			time.sleep(2)
			crt.Screen.Send("crypto isakmp key 6 3BGbNGBPitBEXar address 61.151.249.45  no-xauth " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("int tunnel 102 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("bandwidth 1000 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip address " + tunnel102IP + " 255.255.0.0 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip access-group ALLOW_LOCAL_ONLY out " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip mtu 1400 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp authentication MCDBK03 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp map multicast 61.151.249.45 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp map 169.186.0.1 61.151.249.45 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp network-id 1803 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp holdtime 300 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip nhrp nhs 169.186.0.1 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("ip tcp adjust-mss 1360 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("delay 1000 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("tunnel source " + outTunnelSource + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("tunnel destination 61.151.249.45 " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("tunnel key 1803 " + chr(13))
			time.sleep(0.2)
			if (outEigrpNum == "10"):
				crt.Screen.Send("tunnel protection ipsec profile MCDBeijing shared " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "21"):
				crt.Screen.Send("tunnel protection ipsec profile MCDShanghai shared " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "24"):
				crt.Screen.Send("tunnel protection ipsec profile MCDWuhan shared " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "20"):
				crt.Screen.Send("tunnel protection ipsec profile MCDGuangzhou shared " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "23"):
				crt.Screen.Send("tunnel protection ipsec profile MCDChongqin shared " + chr(13))
				time.sleep(0.2)
				
			crt.Screen.Send("exit " + chr(13))
			time.sleep(0.2)
			
			#查看获取Tunnel102地址
			crt.Screen.Send("do show ip inter brief | include Tunnel102 " + chr(13))
			time.sleep(3)
			ScreenRowTunnel102 = crt.Screen.CurrentRow - 1
			#outTunnel102 获取Tunnel102地址
			outTunnel102 = crt.Screen.Get(ScreenRowTunnel102,28,ScreenRowTunnel102,42)
			#crt.Dialog.MessageBox( outTunnel102)
			time.sleep(0.2)
			
			if (outEigrpNum == "10"):
				crt.Screen.Send("ip route 4.0.0.31 255.255.255.255 tunnel 100 name BJ-POP-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.32 255.255.255.255 tunnel 101 name BJ-POP-CU " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.105 255.255.255.255 tunnel 102 name SH-BK3-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 0.0.0.0 0.0.0.0 tunnel 102 169.186.0.1 220 " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "21"):
				crt.Screen.Send("ip route 4.0.0.10 255.255.255.255 tunnel 100 name SH-POP-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.11 255.255.255.255 tunnel 101 name SH-POP-CU " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.105 255.255.255.255 tunnel 102 name SH-BK3-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 0.0.0.0 0.0.0.0 tunnel 102 169.186.0.1 220 " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "24"):
				crt.Screen.Send("ip route 4.0.0.43 255.255.255.255 tunnel 100 name WU-POP-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.44 255.255.255.255 tunnel 101 name WU-POP-CU " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.105 255.255.255.255 tunnel 102 name SH-BK3-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 0.0.0.0 0.0.0.0 tunnel 102 169.186.0.1 220 " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "20"):
				crt.Screen.Send("ip route 4.0.0.21 255.255.255.255 tunnel 100 name GZ-POP-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.22 255.255.255.255 tunnel 101 name GZ-POP-CU " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.105 255.255.255.255 tunnel 102 name SH-BK3-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 0.0.0.0 0.0.0.0 tunnel 102 169.186.0.1 220 " + chr(13))
				time.sleep(0.2)
			elif (outEigrpNum == "23"):
				crt.Screen.Send("ip route 4.0.0.41 255.255.255.255 tunnel 100 name CD-POP-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.42 255.255.255.255 tunnel 101 name CD-POP-CU " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 4.0.0.105 255.255.255.255 tunnel 102 name SH-BK3-CT " + chr(13))
				time.sleep(0.2)
				crt.Screen.Send("ip route 0.0.0.0 0.0.0.0 tunnel 102 169.186.0.1 220 " + chr(13))
				time.sleep(0.2)
				
			#SLA配置部分	
			crt.Screen.Send("ip sla logging traps " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("snmp-server enable traps syslog " + chr(13))
			time.sleep(0.2)	
			
			crt.Screen.Send("ip sla 120 " + chr(13))
			time.sleep(0.2)	
			if (outEigrpNum == "10"):
				crt.Screen.Send("icmp-jitter 4.0.0.31 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "21"):
				crt.Screen.Send("icmp-jitter 4.0.0.10 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "24"):
				crt.Screen.Send("icmp-jitter 4.0.0.43 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "20"):
				crt.Screen.Send("icmp-jitter 4.0.0.21 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "23"):
				crt.Screen.Send("icmp-jitter 4.0.0.41 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			
			crt.Screen.Send("timeout 6000 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("frequency 10 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("ip sla schedule 120 life forever start-time now " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("ip sla 122 " + chr(13))
			time.sleep(0.2)	
			if (outEigrpNum == "10"):
				crt.Screen.Send("icmp-jitter 4.0.0.32 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "21"):
				crt.Screen.Send("icmp-jitter 4.0.0.11 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "24"):
				crt.Screen.Send("icmp-jitter 4.0.0.44 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "20"):
				crt.Screen.Send("icmp-jitter 4.0.0.22 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
				
			elif (outEigrpNum == "23"):
				crt.Screen.Send("icmp-jitter 4.0.0.42 num-packets 20 interval 40 " + chr(13))
				time.sleep(0.2)
			
			crt.Screen.Send("timeout 6000 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("frequency 10 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("ip sla schedule 122 life forever start-time now " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("ip sla 124 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("icmp-jitter 4.0.0.105 num-packets 40 interval 40 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("timeout 6000 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("frequency 10 " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send("ip sla schedule 124 life forever start-time now " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send(chr(13))
			time.sleep(0.2)
			crt.Screen.Send("do show ip sla summary  " + chr(13))
			time.sleep(5)	
			
			#track部分
			crt.Screen.Send("track 1 ip sla 120  " + chr(13))
			time.sleep(0.2)	
			crt.Screen.Send(" delay down 49 up 1  " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("track 2 ip sla 122    " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send(" delay down 49 up 1  " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("track 3 ip sla 124  " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send(" delay down 47 up 29  " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("track 4 list boolean or    " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" object 1  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" object 2  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("track 5 list boolean or   " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send(" delay down 47 up 29  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" object 1  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" object 2  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" object 3  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(" delay down 80 up 1   " + chr(13))
			time.sleep(15)
			crt.Screen.Send("do show track brief   " + chr(13))
			time.sleep(0.2)
			
			crt.Screen.Send("kron occurrence every30m in 35 recurring system-startup    " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("policy-list eigrp-force-restart   " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("kron policy-list eigrp-force-restart    " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send("cli event manager run eigrp-forceup-timer   " + chr(13))
			time.sleep(0.2)
			
			crt.Screen.Send("snmp-server enable traps syslog   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("event manager applet eigrp-down     " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("event track 4 state down   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 1.0 cli command \"enable\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 2.0 cli command \"config ter\"   " + chr(13))
			time.sleep(0.1)
			if (outEigrpNum == "10"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 10\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "21"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 21\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "24"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 24\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "20"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 20\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "23"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 23\" " + chr(13))
				time.sleep(0.1)
			crt.Screen.Send("action 3.1 cli command \"shutdown\"   " + chr(13))
			crt.Screen.Send("action 4.0 cli command \"end\"   " + chr(13))
			crt.Screen.Send(chr(13))
			crt.Screen.Send("event manager applet alldown     " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("event track 5 state down   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 1.0 cli command \"enable\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 2.0 cli command \"config t\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.0 cli command \"int tunnel 100\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.1 cli command \"shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.2 cli command \"no shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.3 cli command \"int tunnel 101\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.4 cli command \"shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.5 cli command \"no shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.6 cli command \"int tunnel 102\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.7 cli command \"shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 3.8 cli command \"no shut\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 4.0 cli command \"end\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send(chr(13))
			crt.Screen.Send("event manager applet eigrp-forceup-timer authorization bypass   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("event none   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 1.0 cli command \"enable\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 2.0 cli command \"config t\"   " + chr(13))
			time.sleep(0.1)
			if (outEigrpNum == "10"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 10\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "21"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 21\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "24"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 24\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "20"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 20\" " + chr(13))
				time.sleep(0.1)
			elif (outEigrpNum == "23"):
				crt.Screen.Send("action 3.0 cli command \"router eigrp 23\" " + chr(13))
				time.sleep(0.1)
			crt.Screen.Send("action 3.1 cli command \"no shutdown\"   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("action 4.0 cli command \"end\"   " + chr(13))
			time.sleep(0.2)
			
			#access-list
			crt.Screen.Send("ip access-list extended ALLOW_LOCAL_ONLY   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	permit eigrp any any   " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	permit ip "  + outLanFinal  + " 0.0.0.255 any      " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	permit ip "  + outTunnel100 + " 0.0.0.0   any      " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	permit ip "  + outTunnel101 + " 0.0.0.0   any      " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	permit ip "  + outTunnel102 + " 0.0.0.0   any      " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("	deny ip any any  " + chr(13))
			time.sleep(0.1)
			
			crt.Screen.Send("in Tun 100  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("ip access-group ALLOW_LOCAL_ONLY out  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("int tun 101  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("ip access-group ALLOW_LOCAL_ONLY out  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("int tun 102  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("ip access-group ALLOW_LOCAL_ONLY out  " + chr(13))
			time.sleep(0.1)
		
			

			crt.Screen.Send("no username admin privilege 15 secret 0 admincisco  " + chr(13))
			time.sleep(0.2)
			crt.Screen.Send( chr(13))
			crt.Screen.Send("no router eigrp 200  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no int t0  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no int t1  " + chr(13))
			time.sleep(0.1)
			
			crt.Screen.Send("no ip route 114.141.162.101 255.255.255.255 "  + outGw + " track 3  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no ip route 114.141.162.102 255.255.255.255 "  + outGw + " track 3  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no ip route 114.141.162.101 255.255.255.255 "  + outGw    + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no ip route 114.141.162.102 255.255.255.255 "  + outGw    + chr(13))
			time.sleep(0.1)
				
			crt.Screen.Send("no ip route 114.141.162.101 255.255.255.255 Null0 200  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no ip route 114.141.162.102 255.255.255.255 Null0 200  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("ip access-list extended ISP_Firewall  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no permit ip host 114.141.162.102 any  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("no permit ip host 114.141.162.101 any  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("end  " + chr(13))
			time.sleep(0.1)
			crt.Screen.Send("wr  " + chr(13))
			time.sleep(5)
			#--------------------------------------------------------------------------------------------------------------------------			
						
			writelog.write(pingIP + "  OK  "  + "\n")
			
			
			crt.Screen.Send(chr(13) + "exit" + chr(13) )
			time.sleep(4)
			#crt.Screen.Send("quit" + chr(13))
			
		else:
			writelog.write(pingIP + "  time out" + "\n")
			time.sleep(4)
			continue
		
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")