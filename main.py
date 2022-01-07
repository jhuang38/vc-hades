# main


# import modules for voice and pyautogui
import commands
import time
import pydirectinput

def main():
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    # ask for user input to which weapon they are using - mouse timings and other settings may vary with weapon
    # e.g. arthur is very slow, use separate combo timings
    print("Starting")
    commands.clickTopOption()
    print("Completed")

if __name__ == "__main__":
    main()