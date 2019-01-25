'''import win32com.client as win
speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("comeon")
#speak.Speak("你好")
'''

import pyttsx3
en = pyttsx3.init()
en.say("hello world")
en.runAndWait()