```

; Variables
Increments 			:= 20 ; < lower for a more granular change, higher for larger jump in brightness 
CurrentBrightness 	:= GetCurrentBrightNess()

; Hot Keys
F6::ChangeBrightness( CurrentBrightness -= Increments ) ; decrease brightness
F7::ChangeBrightness( CurrentBrightness += Increments ) ; increase brightness

; Functions
ChangeBrightness( ByRef brightness, timeout = 1 )
{
	if ( brightness > 0 && brightness < 100 )
	{
		For property in ComObjGet( "winmgmts:\\.\root\WMI" ).ExecQuery( "SELECT * FROM WmiMonitorBrightnessMethods" )
			property.WmiSetBrightness( timeout, brightness )	
	}
 	else if ( brightness >= 100 )
 	{
 		brightness := 100
 	}
 	else if ( brightness <= 0 )
 	{
 		brightness := 0
 	}
}

GetCurrentBrightNess()
{
	For property in ComObjGet( "winmgmts:\\.\root\WMI" ).ExecQuery( "SELECT * FROM WmiMonitorBrightness" )
		currentBrightness := property.CurrentBrightness	

	return currentBrightness
}

```


