# voice commands for controlling zagreus

# import modules for pydirectinput, time etc.
import pydirectinput
import time
import pyautogui

# commmands for clicking boon/hammer/pom upgrades
def clickTopOption():
    pydirectinput.click(x=909, y=370, clicks=1)

def clickMiddleOption():
    pydirectinput.click(x=909, y=598, clicks=1)

def clickBottomOption():
    pydirectinput.click(x=909, y=817, clicks=1)

def clickReroll():
    pydirectinput.click(x=909, y=937, clicks=1)

# helper to hold keys

def holdKey(key, holdTime):
    pydirectinput.keyDown(key)
    time.sleep(holdTime)
    pydirectinput.keyUp(key)

def moveUp():
    holdKey('w', 1)

def moveDown():
    holdKey('s', 1)

def moveRight():
    holdKey('d', 1)

def moveLeft():
    holdKey('a', 1)

def dashInput():
    pydirectinput.press('space', presses = 2)

def swordFullCombo():
    pydirectinput.press('o', presses = 3)

def swordDashCombo():
    pydirectinput.keyDown('space')
    pydirectinput.keyDown('o')
    pydirectinput.keyUp('space')
    pydirectinput.keyUp('o')
    pydirectinput.press('q')

def useCast():
    pydirectinput.press('p')