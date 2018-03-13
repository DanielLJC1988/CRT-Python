#$language = "Python"
#$interface = "1.0"
import re
import sys
import os
import time
import datetime

now = datetime.datetime.now()
timeNow = now.strftime('%Y.%m.%d')
crt.Screen.Send(chr(13))
crt.Screen.Send('cd /usr/DATA' + chr(13))
crt.Screen.Send('lcd /PythonLog' + chr(13))
crt.Screen.Send('put -r ' + timeNow +  chr(13))