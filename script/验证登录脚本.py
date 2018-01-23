#$language = "Python"
#$interface = "1.0"
import sys
import os



#crt.Screen.Synchronous = True
crt.Screen.IgnoreCase = True
crt.Screen.Send(chr(13))
crt.Screen.WaitForString("Username:")
crt.Screen.Send("lujc" + chr(13))
crt.Screen.WaitForString("Password:",2)

code = os.popen('python c:/Python27/test.py').read()
crt.Screen.Send(code)