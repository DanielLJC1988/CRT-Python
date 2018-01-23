#$language = "VBScript"
#$interface = "1.0"


Sub Main()
crt.Screen.Synchronous = True
crt.screen.WaitForString "main memory"
'crt.screen.SendKeys "^{BREAK}"
crt.screen.SendSpecial "TN_BREAK"
crt.screen.SendSpecial "TN_BREAK"


crt.screen.WaitForString "rommon 1 >"
crt.screen.send "confreg 0x2142" & VbCr

crt.screen.WaitForString "rommon 2 >"
crt.screen.send "reset" & VbCr

crt.screen.WaitForString "[yes/no]:"
crt.screen.send "no" & VbCr
crt.screen.send VbCr
crt.screen.send VbCr
crt.screen.send VbCr
crt.screen.WaitForString ">"
crt.screen.send "en" & VbCr

crt.screen.WaitForString "#"
crt.screen.send "erase startup-config" & VbCr
crt.screen.send VbCr

crt.screen.WaitForString "#"
crt.screen.send "configure terminal" & VbCr

crt.screen.WaitForString "(config)#"
crt.screen.send "config-register 0x2102" & VbCr

crt.screen.WaitForString "(config)#"
crt.screen.send "exit" & VbCr

crt.screen.WaitForString "#"
crt.screen.send "write" & VbCr

crt.screen.WaitForString "#"
crt.screen.send "reload" & VbCr
crt.screen.send VbCr

crt.screen.WaitForString "[yes/no]:"
crt.screen.send "no" & VbCr

crt.screen.send VbCr

End Sub
