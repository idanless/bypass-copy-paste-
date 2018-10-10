#import time
import keyboard
import pyperclip


#pyperclip.paste() - load from clipboard
#keyboard.add_hotkey triger by key combination
#keyboard.write - type like a keyboard


while True:

    clipboard_content = pyperclip.paste()
    keyboard.add_hotkey("left alt+left ctrl+a", print, args=('trigger', clipboard_content))
    keyboard.wait('left alt+left ctrl+a')
    keyboard.write('0'+clipboard_content)
    clipboard_content = pyperclip.paste()