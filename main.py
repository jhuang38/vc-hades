# main.py
# import modules for voice and pyautogui
import commands
import time
import pydirectinput
import speech_recognition
import pyttsx3

def main():
    # dictionary mappings for each command
    # if you want to change the mappings, change the key value that each command is mapped to
    commandLookup = {
        'up': commands.moveUp,
        'down': commands.moveDown,
        'right': commands.moveRight,
        'left': commands.moveLeft,
        'dash': commands.dashInput,
        'hit': commands.useAttack,
        'cast': commands.useCast,
        'special': commands.useSpecial,
        'call': commands.useCall,
        'top': commands.clickTopOption,
        'middle': commands.clickMiddleOption,
        'bottom': commands.clickBottomOption,
        'roll': commands.clickReroll,
        'java': commands.swordDashCombo,
        'python': commands.arthurCombo
    } 
    # ask for user input to which weapon they are using - mouse timings and other settings may vary with weapon
    # e.g. arthur is very slow, use separate combo timings
    print("Starting")
    recognizer = speech_recognition.Recognizer()
    continueLoop = True
    while continueLoop:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                textArray = text.split(' ')
                print("Recognized: " + text)
                # classic for loop to check, as when user inputs, they probably
                # want the first thing they say to be executed first
                for word in textArray:
                    if word in commandLookup.keys():
                        commandLookup[word]()
                    elif word == 'quit':
                        continueLoop = False
                        break
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            print("Unrecognized")
            continue
    print("Completed")

if __name__ == "__main__":
    main()