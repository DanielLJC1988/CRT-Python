#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time

crt.Screen.IgnoreCase = True
fping = open(r"c:/Python27/adidas site.txt")
writelog = open("c:/Python27/adidas site log.txt","a+")
while True:
	linesite = fping.readline()
	#linelog = writelog.write()
	pingIP = str(linesite).strip('\n')
	if linesite:
		writelog.write('INSERT INTO user_auth_perms values (\'4\',\'%s\',\'3\');\n' %(pingIP))
		writelog.write('update host set monitor=\'on\'  where id=\'%s\';\n' %(pingIP))
		writelog.write('\n')
	else:
		break
fping.close()
writelog.close()
crt.Dialog.MessageBox("Script completed")