import keyboard
import pyperclip
import time



while True:
    clipboard_content = pyperclip.paste()
    keyboard.add_hotkey("left alt+left ctrl+a", print, args=('trigger', clipboard_content))
    keyboard.write('\t' + clipboard_content)
    keyboard.wait('left alt+left ctrl+a')
