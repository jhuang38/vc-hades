# voice commands for controlling zagreus

# import modules for pydirectinput, time etc.
import pydirectinput
import time 
import win32api, win32con

# helper to click, as pyadirectinput doesn't work for whatever reason
def click(x, y, button):
    # special case: if both x and y are -1, then do not change position
    if x != -1 and y != -1:
        win32api.SetCursorPos((x, y))
    if button == 'right':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# helper to hold keys
def holdKey(key, holdTime):
    pydirectinput.keyDown(key)
    time.sleep(holdTime)
    pydirectinput.keyUp(key)

# commmands for clicking boon/hammer/pom upgrades
def clickTopOption():
    click(909, 370, 'left')

def clickMiddleOption():
    click(909, 598, 'left')

def clickBottomOption():
    click(909, 817)

def clickReroll():
    click(946, 937)

# commands for movement and combat
def moveUp():
    holdKey('w', 0.5)

def moveDown():
    holdKey('s', 0.5)

def moveRight():
    holdKey('d', 0.5)

def moveLeft():
    holdKey('a', 0.5)

def dashInput():
    pydirectinput.press('space', presses = 2)

def useAttack():
    click(-1, -1, 'left')

def useSpecial():
    pydirectinput.press('q')

def useCast():
    click(-1, -1, 'right')

def useCall():
    pydirectinput.press('f')

def interact():
    pydirectinput.press('e')

def summon():
    pydirectinput.press('1')

## SPECIALIZED INPUTS
# for aspect of arthur, 0.45 seems good
# for other aspects, use 0.2
def swordFullCombo(timeBetweenClicks):
    for i in range(3):
        click(-1, -1, 'left')
        time.sleep(timeBetweenClicks)

def swordDashCombo():
    pydirectinput.keyDown('space')
    click(-1, -1, 'left')
    pydirectinput.keyUp('')
    pydirectinput.press('q')

def arthurCombo():
    swordFullCombo(0.45)
