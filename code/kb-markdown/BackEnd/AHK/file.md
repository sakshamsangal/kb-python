```

fn1 := "temp"
F9::setFileName()

setFileName() {
    global fn1
    fn := InputBox("Enter file name.", "File name", "w640 h480")
    if (fn.Result = "OK") {
        fn1 := fn.Value
    }
    else{
        MsgBox "You entered '" fn.Value "' but then cancelled."
    }

}
F8::{

    A_Clipboard := "" ; Empty the clipboard
    Send "^c"
    if !ClipWait(2)
    {
        MsgBox "The attempt to copy text onto the clipboard failed."
        return
    } else{
        FileAppend "``````" . "`n`n" . A_Clipboard . "`n`n```````n`n`n", "C:\Users\saksangal\Documents\saksham\document\lang\front_end\kb4\" . fn1 . ".md" 
    }
}

;Run "notepad++"
;WinActive("ahk_class Notepad")
;FileAppend ClipboardAll() . "`n", "C:\Users\saksangal\Documents\saksham\document\text\temp.txt" 
;WinActive("C:\Users\saksangal\Documents\saksham\document\text\temp.txt", , 2)
;Send "^v"


```


