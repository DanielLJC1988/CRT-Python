#$language = "VBScript"
#$interface = "1.0"

crt.Screen.Synchronous = True

' This automatically generated script may need to be
' edited in order to work correctly.

Sub Main
	crt.Screen.WaitForString "Username: "
	crt.Screen.Send "fashion" & chr(13)
	crt.Screen.WaitForString "Password: "
	crt.Screen.Send "fashion@123" & chr(13)
	crt.Screen.WaitForStrings "VPNServer-CT-3945>","VPNServer-CU-3945>"
	crt.Screen.Send "en" & chr(13)
	crt.Screen.WaitForString "Password: "
	crt.Screen.Send "fashion@123" & chr(13)
End Sub
