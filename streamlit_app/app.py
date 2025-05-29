import streamlit as st
import requests

st.set_page_config(page_title="📊 Voice Market Assistant", layout="centered")
st.title("🧠 Voice-Based Finance Assistant")

col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Text Query"):
        response = requests.get("http://localhost:8000/brief")
        if response.status_code == 200:
            st.success(response.json()["brief"])
        else:
            st.error("Failed to fetch response.")

with col2:
    if st.button("🎤 Speak My Query"):
        with st.spinner("Listening and thinking..."):
            response = requests.get("http://localhost:8000/voice-brief")
            if response.status_code == 200:
                result = response.json()
                st.info(f"🎧 You said: {result['query']}")
                st.success(f"🗣️ Response: {result['brief']}")
            else:
                st.error("Something went wrong.")
