import streamlit as st
import speech_recognition as sr

def transcribe_speech(recognizer, microphone, api_choice, language):
    with microphone as source:
        st.info("Listening... Speak now!")
        audio = recognizer.listen(source)
        st.info("Transcribing...")

    try:
        if api_choice == "Google":
            text = recognizer.recognize_google(audio, language=language)
        elif api_choice == "Sphinx":
            # Note: sphinx supports only limited languages, usually 'en-US'
            text = recognizer.recognize_sphinx(audio, language=language)
        else:
            text = "Selected API not implemented."
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

