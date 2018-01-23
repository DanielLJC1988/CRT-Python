#$language = "Python"
#$interface = "1.0"
import os

crt.Screen.IgnoreCase = True
username = crt.Dialog.Prompt("enter username","For example  youhe or youheA","",False)
ipStart = crt.Dialog.Prompt("Enter start IP ","IP START","",False)
ipEnd = crt.Dialog.Prompt("Enter end IP"," IP END","",False)

f1 = open("c:/Python27/b.txt",'w')
a = int(ipStart)
b = int(ipEnd)
c = b + 1
for i in range(a,c):
	if username == 'youhe':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'youhe%d\', \'123456\', \'169.3.16.%d\', \'VPDN_10217_youhe\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'youheA':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'youheA%d\', \'123456\', \'169.5.14.%d\', \'VPDN_10217_youhe\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'maidanglao':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'maidanglao%d\', \'123456\', \'169.7.11.%d\', \'maidanglao\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'ruanyinA':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'ruanyinA%d\', \'123456\', \'169.6.12.%d\', \'ruanyin\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'hemei4G':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'hemei4G%d\', \'123456\', \'169.5.7.%d\', \'hemei\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'hemei4GA':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'hemei4GA%d\', \'123456\', \'169.5.26.%d\', \'hemei\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'adidaswifi':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'adidaswifi%d\', \'123456\', \'169.4.26.%d\', \'adidaswifi\', \'active\');\n' %(i,i))
			a += 1
	elif username == 'ceshi':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'ceshi%d\', \'123456\', \'169.4.19.%d\', \'vpdn_20003_Internet\', \'inactive\');\n' %(i,i))
			a += 1
	elif username == 'dingyong':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'dingyong%d\', \'123456\', \'169.4.20.%d\', \'vpdn_20003_Internet\', \'inactive\');\n' %(i,i))
			a += 1
	elif username == 'qiangxiu':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'qiangxiu%d\', \'123456\', \'169.4.21.%d\', \'vpdn_20003_Internet\', \'inactive\');\n' %(i,i))
			a += 1
	elif username == 'scbchinawifi':
		if i <= b:
			f1.write('insert into fashion_cm (username, password, ip, groupname, status) values (\'scbchinawifi%d\', \'123456\', \'169.4.28.%d\', \'wifi_40001_scbchina\', \'active\');\n' %(i,i))
			a += 1