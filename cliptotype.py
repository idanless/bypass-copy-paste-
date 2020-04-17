import keyboard
import pyperclip
import time

class Key:
    def __init__(self,clip="test"):
        self.keywait = keyboard.wait('left ctrl+q')
        self.clip = clip
        self.write = keyboard.write('\t')

class Shoot:
    def __init__(self,clip="test"):
        self.clip = clip
        self.write = keyboard.write(self.copyclip())

    def copyclip(self):
        clipboard_content = pyperclip.paste()
        clipboard_content =  clipboard_content.rstrip()
        print("write words numbers ", len(clipboard_content) , "\n")
        print("copy print :", clipboard_content)
        return clipboard_content

    def getclip(self):
        return self.copyclip()


while True:
    key = Key()
    key2 = Shoot()
    key.keywait
    key.write
    key2.write
