import streamlit as st
import requests
import json

st.title("Basho AI - Haiku Edition")

# Text input for the user's prompt
user_question = st.text_input("Ask the AI anything:")

# Button to send the request
if st.button("Send"):
    if user_question:
        # Enhanced prompt that instructs the AI to respond in haiku format
        haiku_prompt = f"Answer this question with a relevant haiku (5-7-5 syllable format). Put each line on a separate line: {user_question}"
        
        # Make API call to local Ollama
        response = requests.post(
            "http://localhost:11434/api/generate",
            headers={"Content-Type": "application/json"},
            json={
                "model": "llama3.2",
                "prompt": haiku_prompt,
                "stream": False
            }
        )
        
        # Display the response
        if response.status_code == 200:
            result = response.json()
            st.write("**AI Response (Haiku):**")
            # Display with preserved line breaks
            st.text(result["response"])
        else:
            st.error("Error connecting to AI")
    else:
        st.warning("Please enter a question")