#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import wolframalpha
client = wolframalpha.Client("API KEY HERE")
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("cmdmp3 audio.mp3")
 
def recordAudio():
    	# Record Audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
	 
	# Speech recognition using Google Speech Recognition
	try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		return "no understand"
	except sr.RequestError as e:
		return "error"
def jarvis(data):
	res = client.query(data)
	speak(next(res.results).text)
# initialization
time.sleep(2)
speak("Hi noah, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)