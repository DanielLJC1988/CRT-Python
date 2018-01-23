#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time


crt.Screen.IgnoreCase = True
crt.Screen.WaitForString("#")
crt.Screen.Send("mysql -u root -p \r\n")
crt.Screen.WaitForString("password")
crt.Screen.Send("fashionmonitorsystem\r\n")
crt.Screen.WaitForStrings("mysql>")
crt.Screen.Send("use cmradius;\r\n")
crt.Screen.WaitForString("mysql>")
crt.Screen.Send("select * from fashion_cm order by id;\r\n")
#crt.Screen.WaitForString("#")



