import speech_recognition as sr


# Function to capture and recognize voice input
def get_voice_input(microphone, recognizer):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
    print("Processing...")
    try:
        text = recognizer.recognize_google(audio, language="en-US" or "it-IT")
    except Exception as e:
        print(f"Error: {e}")
        text = ""
    return text




