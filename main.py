# main


# import modules for voice and pyautogui
import commands
import time
import pydirectinput

def main():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print("Starting")
    time.sleep(1)
    for i in range(3):
        pydirectinput.click(button='right')
        commands.swordFullCombo()
    print("completed")

if __name__ == "__main__":
    main()