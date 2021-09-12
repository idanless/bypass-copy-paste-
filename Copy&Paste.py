import argparse
from time import sleep
from pyautogui import write
from pyperclip import paste
import sys



cm = ''



def delay(delay):
   print('will send the key when this reach to 100%')
   sleep(delay)
   for i in range(100 + 1):
       sleep(0.1)
       sys.stdout.write(('=' * i) + ('' * (100 - i)) + ("\r [ %d" % i + "% ] "))
       sys.stdout.flush()



def clipfound():
    clipboard_content = paste()
    clipboard_content = str(clipboard_content)
    return clipboard_content

def keyboed(clipboard_content):
    write(clipboard_content, interval=0.1)


def read(delay):
    global cm
    delay(delay)
    with open('command.txt') as f:
        lines = f.read()
    cm = lines
    keyboed(cm)


def main():
    parser = argparse.ArgumentParser(description='Bypass Copy&paste by idan less v1.0')
    parser.add_argument('-s',"--start", help="start", nargs='?', const=1)
    parser.add_argument('-d', '--delay', type=int, help='delay until the script shoot the text as keyboard event will be default 5 sec',default=5)
    parser.add_argument('-c', '--clip', type=bool, help='if true the script read the clip and make keyboard event will be default as True',default=True)
    parser.add_argument('-r', '--read', type=bool, help='if true the script will try found "command.txt and read from it" ')

    args = parser.parse_args()
    print('delay:', args.delay, 'clip', args.clip)
    if args.clip and args.read != True:
        clip = clipfound()
        delay(args.delay)
        keyboed(clip)
        print('\n')
        print('sendkey\n',clip)
    else:
        read(args.delay)


if __name__== '__main__':
    main()
