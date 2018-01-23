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
crt.Screen.Send("ping 10.188.209.31  re 10000\n")
start = time.clock()
crt.Screen.WaitForString("#")
end = time.clock()
crt.Dialog.MessageBox("time: %f s" % (end - start))
