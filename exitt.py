from time import sleep
import pyautogui as gui
from datetime import datetime, time

from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

QUIT_TIME = time(16, 0)

def main():
    while True:
        if datetime.now().time() >= QUIT_TIME:
            position = gui.locateOnScreen('leave.png', confidence=0.9)
            gui.leftClick(position)
            print(position)
            break

main()