import pyttsx3
friend = pyttsx3.init()
speech = input("Type something:",)
friend.say(speech)
friend.save_to_file(speech, 'speech.mp3')
friend.runAndWait()