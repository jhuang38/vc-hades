# main.py
# import modules for voice and pyautogui
import commands
import time
import pydirectinput
import speech_recognition
import pyttsx3

def main():
    # ask for user input to which weapon they are using - mouse timings and other settings may vary with weapon
    # e.g. arthur is very slow, use separate combo timings
    print("Starting")
    commands.clickTopOption()
    

    recognizer = speech_recognition.Recognizer()
    continueLoop = True
    while continueLoop:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.01)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                textArray = text.split(' ')
                print("Recognized: " + text)
                # classic for loop to check, as when user inputs, they probably
                # want the first thing they say to be executed first
                for word in textArray:
                    if word == 'quit':
                        continueLoop = False
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue
    print("Completed")

if __name__ == "__main__":
    main()