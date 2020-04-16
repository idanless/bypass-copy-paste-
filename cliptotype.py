import keyboard
import pyperclip
import time



while True:
    time.sleep(1)
    keyboard.wait('left alt+left ctrl+a')
    clipboard_content = pyperclip.paste()
    clipboard_content.split()
    print("write this ",clipboard_content)
    keyboard.write(clipboard_content)
