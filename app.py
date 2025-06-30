import streamlit as st
import speech_recognition as sr
from my_recognition import transcribe_speech


def main():
    st.title("Improved Speech Recognition App")

    st.sidebar.header("Settings")
    api_choice = st.sidebar.selectbox("Select Speech Recognition API", ["Google", "Sphinx"])
    language = st.sidebar.selectbox("Select Language", [
        "en-US", "fr-FR", "es-ES", "de-DE", "it-IT", "pt-PT", "zh-CN", "ja-JP", "ko-KR"
    ])
    st.sidebar.write("Note: Sphinx supports mostly English.")

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    if "transcribed_text" not in st.session_state:
        st.session_state.transcribed_text = ""

    # Buttons to control recording
    col1, col2, col3 = st.columns(3)
    with col1:
        start = st.button("Start Recording")
    with col2:
        clear = st.button("Clear Transcription")
    with col3:
        save = st.button("Save Transcription")

    if start:
        text = transcribe_speech(recognizer, microphone, api_choice, language)
        if text:
            st.session_state.transcribed_text += text + "\n"

    if clear:
        st.session_state.transcribed_text = ""

    st.text_area("Transcribed Text", value=st.session_state.transcribed_text, height=200)

    if save and st.session_state.transcribed_text.strip():
        # Create downloadable file
        st.download_button(
            label="Download Transcription as TXT",
            data=st.session_state.transcribed_text,
            file_name="transcription.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()
