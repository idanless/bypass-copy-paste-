import keyboard
import pyperclip
import time

class Key:
    def __init__(self,clip="test"):
        self.keywait = keyboard.wait('left alt+left ctrl+a')
        self.clip = clip
        self.write = keyboard.write(self.copyclip())

    def copyclip(self):
        clipboard_content = pyperclip.paste()
        clipboard_content.split()
        print("write this ", clipboard_content)
        return clipboard_content

    def getclip(self):
        return self.copyclip()



while True:
    key = Key()
    key.keywait
    key.write
