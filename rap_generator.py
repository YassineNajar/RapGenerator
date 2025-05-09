import streamlit as st
import requests

st.title("🎤 Free AI Rap Generator (Local LLM)")

topic = st.text_input("Enter topic (e.g. love, ambition):")
mood = st.selectbox("Mood", ["Chill", "Hype", "Sad", "Dark"])
length = st.selectbox("Length", ["Short", "Medium", "Long"])
style = st.selectbox("Style", ["Old School", "Trap", "Freestyle"])

if st.button("Generate"):
    prompt = f"""
    You are a rapper. Write a {length.lower()} rap about "{topic}" in a {mood.lower()} mood and {style.lower()} style.
    Include rhymes and a chorus.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.ok:
        st.text_area("🎵 Lyrics:", response.json()["response"], height=400)
    else:
        st.error("Failed to connect to the local LLM. Is Ollama running?")
