# vc-hades
Controls for playing Hades with only voice chat. This program was made with an 1920x1080 screen in mind, and it assumes you are using the default keyboard and mouse controls.

## Why?
After watching many of the YouTuber/streamer DougDoug's gaming challenges, I was inspired to create a program which would allow me to do something similar. Thus, I picked Hades, one of my favourite games, to implement voice controls to. 

## How does it work?
This program works by converting a voice input from the user to text using the PyAudio, SpeechRecognition, and pyttsx3 libraries. By searching through the output string, whenever it finds a recognized command keyword, it will perform the action associated with said keyword by using the pydirectinput library for keyboard inputs and pywin32 module for mouse clicks.

## Controls
These are laid out in main.py. If you decide to clone this repo and try this by yourself, you can edit the voice mappings there. The ones I have used are listed here:

### General Controls
- Move Right: 'right'
- Move Up: 'up'
- Move Left: 'left'
- Move Down: 'down'
- Dash: 'dash'
- Default Attack: 'hit'
- Special: 'special'
- Cast: 'cast'
- Click Top Option: 'top'
- Click Middle Option: 'middle'
- Click Bottom Option: 'bottom'
- Reroll: 'reroll'
- Call: 'call'
- Summon: 'summon'

### Specialized Controls
- Regular Stygius damage cycle (dashA + special): 'java'
- Aspect of Arthur full combo: 'python'

## Potential future features:
- mouse control
- support for different screen sizes
- AI learns to play Hades (very far in the future, I will need to learn more about the details of ML
