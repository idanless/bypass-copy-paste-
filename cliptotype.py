import keyboard
import pyperclip
import time



while True:
    time.sleep(1)
    keyboard.wait('left alt+left ctrl+a')
    clipboard_content = pyperclip.paste()
    keyboard.add_hotkey("left alt+left ctrl+a", print, args=('trigger', clipboard_content))
    keyboard.write('\t' + clipboard_content)
    time.sleep(1)
