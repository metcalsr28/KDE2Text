from subprocess import check_output
import os

os.system('spectacle -rb -o "output.png"')

import cv2
img = cv2.imread('output.png')
height, width, channels = img.shape

if width >= height:
    test = check_output(['wine', 'res/Capture2Text/Capture2Text_CLI.exe', '-l' ,'Japanese', '-i', 'output.png']).decode("utf8")
else:
    test = check_output(['wine', 'res/Capture2Text/Capture2Text_CLI.exe', '-l' ,'Japanese', '--vertical', '-i', 'output.png']).decode("utf8")

import pyperclip
pyperclip.copy(test)
spam = pyperclip.paste()
