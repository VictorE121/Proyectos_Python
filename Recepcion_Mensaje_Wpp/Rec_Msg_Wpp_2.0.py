from win32gui import GetWindowText, GetForegroundWindow as FW
import keyboard as kb
import time

time.sleep(1)

current_window = GetWindowText(FW())



if current_window != 'SAP Logon 770':
    kb.press_and_release('alt + tab')
    print(current_window)
    time.sleep(5)
else:
    print("Ventana encontrada: ", current_window)
