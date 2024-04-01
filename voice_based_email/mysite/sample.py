import speech_recognition as sr

def audio_to_text():
    """Converts spoken audio to text using Google Speech Recognition.

    Handles exceptions for unknown values and request errors.

    Returns:
        str: The recognized text, or None if an error occurs.
    """

    recognizer = sr.Recognizer()

    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            print("Speak something...")
            # Adjust for ambient noise to improve accuracy
            recognizer.adjust_for_ambient_noise(source)
            # Listen to the user's input
            audio_data = recognizer.listen(source)

            print("Processing.a..")

            # Use Google Speech Recognition to convert audio to text
            text = recognizer.recognize_google(audio_data)
            return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError as e:
        print("Sorry, an error occurred while processing your request; {0}".format(e))
        return None

# Call the function to start the process
recognized_text = audio_to_text()

if recognized_text is not None:
    print("Converted text:")
    print(recognized_text)
