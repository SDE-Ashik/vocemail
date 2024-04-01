# # # import speech_recognition as sr
# # # r = sr.Recognizer()
# # # with sr.Microphone() as source:
# # #     r.adjust_for_ambient_noise(source, duration=1)
# # #     playsound('speak.mp3')
# # #     audio = r.listen(source, phrase_time_limit=20)
# # #     playsound(audio)


# # # # import speech_recognition as sr
# # # # from playsound import playsound

# # # # # Create a recognizer object
# # # # r = sr.Recognizer()

# # # # # Adjust for ambient noise
# # # # with sr.Microphone() as source:
# # # #     print("Adjusting for ambient noise...")
# # # #     r.adjust_for_ambient_noise(source, duration=1)
# # # #     print("Speak now...")

# # # #     # Record audio from the microphone
# # # #     audio = r.listen(source, timeout=20)  # Set a timeout of 20 seconds

# # # #     # Save the recorded audio to a file (optional)
# # # #     with open("recorded_audio.wav", "wb") as f:
# # # #         f.write(audio.get_wav_data())

# # # # # Play the recorded audio
# # # # print("Playing recorded audio...")
# # # # playsound("recorded_audio.wav")


# # import speech_recognition as sr

# # # Create a recognizer object
# # r = sr.Recognizer()

# # # Adjust for ambient noise
# # with sr.Microphone() as source:
# #     print("Adjusting for ambient noise...")
# #     r.adjust_for_ambient_noise(source, duration=1)
# #     print("Speak now...")

# #     # Record audio from the microphone
# #     audio = r.listen(source, timeout=20)  # Set a timeout of 20 seconds

# # # Recognize speech using Google Speech Recognition
# # try:
# #     print("Transcribing audio...")
# #     text = r.recognize_google(audio)
# #     print("Transcription:", text)
# # except sr.UnknownValueError:
# #     print("Google Speech Recognition could not understand the audio.")
# # except sr.RequestError as e:
# #     print("Could not request results from Google Speech Recognition service; {0}".format(e))
# import speech_recognition as sr

# # Create a recognizer object
# r = sr.Recognizer()

# # Use a microphone as source
# with sr.Microphone() as source:
#     print("Speak something...")

#     # Adjust for ambient noise
#     r.adjust_for_ambient_noise(source)

#     # Listen for audio input
#     audio = r.listen(source)

# # Recognize speech using Google Speech Recognition
# try:
#     print("Recognizing...")
#     text = r.recognize_google(audio)
#     print("You said:", text)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand the audio.")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
# 


import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

def listen_and_convert():
  """
  This function listens to microphone input and converts it to text using Google Speech-to-Text API.
  """
  with sr.Microphone() as source:
    print("Speak anything ...")
    audio_text = r.listen(source)
    
    try:
      # Recognize speech using Google Speech Recognition
      text = r.recognize_google(audio_text)
      print("You said: {}".format(text))
    except sr.UnknownValueError:
      print("Sorry could not understand audio")
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Run the function to listen and convert
listen_and_convert()
