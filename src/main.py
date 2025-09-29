import voice_input as vi
import nlp_basic_rules as nlp
import speech_recognition as sr

recognizer_instance = sr.Recognizer()
microphone_instance = sr.Microphone()


if __name__ == "__main__":
    text_recognized = vi.get_voice_input(microphone_instance, recognizer_instance)
    print(f"Final recognized text: {text_recognized}")
    intent = nlp.get_intent(text_recognized)
    print(f"Identified intent: {intent}")